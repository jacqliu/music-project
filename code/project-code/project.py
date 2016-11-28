#project

import sys
sys.path.append('..')
from common.core import *
from common.audio import *
from common.mixer import *
from common.wavegen import *
from common.wavesrc import *
from common.gfxutil import *
from common.note import *
from common.trail import *

from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.graphics import PushMatrix, PopMatrix, Translate, Scale, Rotate
from kivy.clock import Clock as kivyClock
from common.kivyparticle import ParticleSystem

import random
import numpy as np
import bisect

# appropriate files
# takemeout_solo = "../../TakeMeOut_solo.wav"
tmo_sfx = "../../sfx.txt"
#wav_file = "../../mirror_mirror.wav"
wav_file = "../../xion.wav"
#gems_path = "../../mirror_mirror_gems.txt"
gems_path = "../../xion.txt"
barline_path = "../../mirror_mirror_gems.txt"

# some colors in hsv
red = (0,1,1)
lime = (1./3, 1,1)
blue = (2./3, 1,1)
yellow = (1./6, 1,1)
cyan = (.5,1,1)
colors = [red, lime, blue, yellow, cyan]
white = (0,0,1)

time_len = 200

class MainWidget(BaseWidget) :
    def __init__(self):
        super(MainWidget, self).__init__()
        # text for scoring
        self.info = topleft_label()
        self.add_widget(self.info)

        # audio controller
        self.audioctrl = AudioController(wav_file)

        # keep track of objects
        self.objects = AnimGroup()
        self.canvas.add(self.objects)

        # keep track of song and data
        self.song = SongData()
        self.song.read_data(gems_path, barline_path)
        gem_data = self.song.get_gems()
        barlines_data = self.song.get_barlines()

        # particle system
        self.ps = ParticleSystem('particle/particle.pex')
        self.add_widget(self.ps)

        #trail display - must be before beat match display, otherwise will translate.... lol
        self.trail_display = TrailDisplay()
        self.objects.add(self.trail_display)

        # display
        self.display = BeatMatchDisplay(gem_data, barlines_data, self.ps)
        self.objects.add(self.display)

        # player
        self.player = Player(self.song, self.display, self.audioctrl, self.trail_display)

        self.paused = True

    def on_key_down(self, keycode, modifiers):
        # play / pause toggle
        if keycode[1] == 'p':
            self.paused = not self.paused

        elif keycode[1] == 'm':
            self.player.on_button_down(None, True)

    def on_touch_down(self, touch):
        self.player.on_button_down(touch.pos, False)

    def on_touch_move(self, touch):
        self.player.on_trigger_hold(touch.pos)

    def on_touch_up(self, touch):
        self.player.on_button_up(touch.pos)

    def on_key_up(self, keycode):
        pass
        
    def on_update(self) :
        self.info.text = '\n\n\nScore: '+ str(self.player.score)
        self.info.text += '\nGenerators: ' + str(len(self.objects.objects))
        self.info.text += '\nStreak: ' + str(self.player.streak)
        self.info.text += '\nBonus: ' + str(self.player.bonus) + 'x \n\n'
        self.info.text += str(self.trail_display)

        if not self.paused:
            self.player.on_update()
            self.objects.on_update()
        else:
            self.info.text += '\n\nPress p to start!'


# creates the Audio driver
# creates a song and loads it with solo and bg audio tracks
# creates snippets for audio sound fx
class AudioController(object):
    def __init__(self, song):
        super(AudioController, self).__init__()
        self.audio = Audio(2)
        self.mixer = Mixer()
        self.audio.set_generator(self.mixer)
        self.song = WaveGenerator(WaveFile(song))

        self.mixer.add(self.song)


    # start / stop the song
    def toggle(self):
        self.song.play_toggle()

    # mute / unmute the solo track
    def set_mute(self, mute):
        if mute:
            self.song.set_gain(0.5)
        else:
            self.song.set_gain(1)

    # play a sound-fx (miss sound)
    def play_sfx(self):
        note = NoteGenerator(90, .5, .2)
        # buf = make_wave_buffers(tmo_sfx, takemeout_solo)['sound']
        self.mixer.add(note)

    # needed to update audio
    def on_update(self):
        self.audio.on_update()


# holds data for gems and barlines.
class SongData(object):
    def __init__(self):
        super(SongData, self).__init__()
        self.gems = []
        self.barlines = []

    # read the gems and song data. You may want to add a secondary filepath
    # argument if your barline data is stored in a different txt file.
    def read_data(self, gem_file, barline_file):
        # get gems
        with open(gem_file) as f:
            content = f.readlines()
        for line in content:
            time, note = line.split('\t')
            self.gems.append((time, note))

        # get barlines
        with open(barline_file) as f:
            content = f.readlines()
        for line in content:
            time, note = line.split('\t')
            self.barlines.append(time)

    def get_gems(self):
        return self.gems

    # return a sublist of the gems that match this time slice:
    def get_gems_in_range(self, start_time, end_time):
        time_slice = []
        for (t, n) in self.gems:
            if start_time <= float(t) <= end_time:
                time_slice.append((t,n))
        return time_slice

    # get index of gem
    def get_gem_index(self, (t,n)):
        return self.gems.index((t,n))

    # get barlines
    def get_barlines(self):
        return self.barlines

    # return a sublist of the barlines that match this time slice:
    def get_barlines_in_range(self, start_time, end_time):
        time_slice = []
        for t in self.gems:
            if start_time <= t <= end_time:
                time_slice.append(t)
        return time_slice


# display for a single gem at a position with a color (if desired)
class GemDisplay(InstructionGroup):
    def __init__(self, pos, color):
        super(GemDisplay, self).__init__()

        self.time = 0

        self.pos = pos
        self.color = Color(hsv=color)
        self.add(self.color)
        self.gem = CEllipse(cpos = self.pos, size = (23, 23), segments = 40)
        self.add(self.gem)

        self.here = True
        self.stop = 0

        self.miss = False
        
    # change to display this gem being hit
    def on_hit(self):
        if not self.miss: 
            self.here = False
            self.stop = self.time + .2

    # change to display a passed gem
    def on_pass(self):
        # change color of gem if missed
        self.miss = True
        # self.remove(self.color)
        # self.remove(self.gem)
        new = (self.color.hsv[0], self.color.hsv[1], .5)
        self.color.h, self.color.s, self.color.v = new
        #self.add(Color(hsv=new))
        #self.add(self.gem)

    # useful if gem is to animate
    def on_update(self, dt):
        self.time += dt
        if not self.here and self.gem.size != (0,0):
            self.gem.size = (0,0)
            self.remove(self.gem)

        return self.here


# Displays one button on the nowbar
class ButtonDisplay(InstructionGroup):
    def __init__(self, ps):
        super(ButtonDisplay, self).__init__()

        self.ps = ps

    # displays when button is down (and if it hit a gem)
    def on_down(self, hit, coords):
        if hit:
            self.ps.emitter_x = coords[0]
            self.ps.emitter_y = coords[1]
            self.ps.start()

    # back to normal state
    def on_up(self):
        self.ps.stop()

    def on_update(self, dt):
        pass

class HealthDisplay(InstructionGroup):
    def __init__(self):
        super(HealthDisplay, self).__init__()
        self.health_left = 100.0

        self.health_bar = Line(points = [0, Window.height, Window.width*self.health_left/100.0, Window.height], width = 30, cap = 'none')
        self.damage_bar = Line(points = [Window.width*self.health_left/100.0, Window.height, Window.width, Window.height], width = 30, cap = 'none')
        self.add(Color(hsv = yellow))
        self.add(self.health_bar)
        self.add(Color(hsv = lime))
        self.add(self.damage_bar)

    def on_hit(self, frac):
        self.health_left -= 100*frac
        self.health_bar.points = [0, Window.height, Window.width*self.health_left/100.0, Window.height]
        self.damage_bar.points = [Window.width*self.health_left/100.0, Window.height, Window.width, Window.height]

    def on_gain(self, frac):
        self.health_left += 100*frac
        self.health_bar.points = [0, Window.height, Window.width*self.health_left/100.0, Window.height]
        self.damage_bar.points = [Window.width*self.health_left/100.0, Window.height, Window.width, Window.height]

# Displays all game elements: Nowbar, Buttons, BarLines, Gems.
# scrolls the gem display.
# controls the gems and nowbar buttons
class BeatMatchDisplay(InstructionGroup):
    def __init__(self, gem_data, barline_data, ps):
        super(BeatMatchDisplay, self).__init__()

        self.time = 0

        # make lanes and nowbar
        self.color = Color(hsv=(0,0,1))
        self.add(self.color)

        # only 2 lanes
        self.lanes = []
        for i in range(Window.height-60, Window.height, 30):
            line = Line(points=[0, i, 800, i])
            self.lanes.append(line)
            self.add(line)

        self.now_bar = Line(points=[100, Window.height-60, 100, Window.height-30], width=1) #TODO - switch to relative to height of window
        self.add(self.now_bar)
        
        # make button for now bar
        self.button = ButtonDisplay(ps)

        #make health bar
        self.health = HealthDisplay()
        self.add(self.health)

        # set up translation
        self.translate = Translate()
        self.add(self.translate)

        # make barlines
        # self.barlines_raw = barline_data
        # self.barlines = []
        # for (t) in self.barlines_raw:
        #     l = Line(points=[float(t)*time_len+100, 540, float(t)*time_len+100, 570])
        #     self.barlines.append(l)
        #     self.add(l)

        # make gems
        self.gems_raw = gem_data
        self.gems = []
        for (t,_) in self.gems_raw:
            # make gem in correct lane and location
            pos = [float(t)*time_len+100, 555]

            c = colors[0]
            g = GemDisplay(pos, c)
            self.gems.append(g)
            self.add(g)

    # called by Player. Causes the right thing to happen
    def gem_hit(self, gem_idx):
        self.gems[gem_idx].on_hit()

    # called by Player. Causes the right thing to happen
    def gem_pass(self, gem_idx):
        self.gems[gem_idx].on_pass()

    # called by Player. Causes the right thing to happen
    def on_button_down(self, hit, coords):
        self.button.on_down(hit, coords)

    # called by Player. Causes the right thing to happen
    def on_button_up(self):
        self.button.on_up()

    # call every frame to make gems and barlines flow down the screen
    def on_update(self, dt) :
        for g in self.gems:
            g.on_update(dt)
        self.time += dt

        # every second is time_len coords height wise
        self.translate.x = -self.time*time_len


# Handles game logic and keeps score.
# Controls the display and the audio
class Player(object):
    def __init__(self, song, display, audio_ctrl, trail_display):
        super(Player, self).__init__()

        self.display = display
        self.trail_display = trail_display
        self.trail_display.callback = self.cast_spell
        self.audio_ctrl = audio_ctrl

        self.song = song
        self.gem_data = self.song.get_gems()
        self.barlines_data = self.song.get_barlines()

        # if need muting
        self.keeper = 0

        # score mechanics
        self.score = 0
        self.streak = 0
        self.bonus = 1

    # called by MainWidget
    def on_button_down(self, pos, push):
        t = self.display.time

        hit = False

        # check if any gems hit
        coords = None
        idx=None
        hits = self.song.get_gems_in_range(t-.1, t+.1)
        for h in hits:
            idx = self.song.get_gem_index(h)
            coords = self.display.gems[idx].pos
            #print coords
            hit = True

        self.display.on_button_down(hit, coords)
        
        if hit:
            self.trail_display.on_touch_down(pos, push)

            # start playing solo again if hit
            #self.audio_ctrl.set_mute(False)
            self.display.gem_hit(idx)

            # score mechanics
            self.streak += 1
            self.score += self.bonus * 100
            self.bonus = self.streak / 10 + 1
        else:
            # if hit is in the wrong lane, pass the gem and play sound
            if idx != None:
                self.display.gem_pass(idx)
                #self.audio_ctrl.play_sfx()

            self.trail_display.on_miss()

            #score mechanics
            self.streak = 0
            self.bonus = 1

    #called by MainWidget
    def on_trigger_hold(self, pos):
        self.trail_display.on_trigger_hold(pos)

    # called by MainWidget
    def on_button_up(self, pos):
        self.display.on_button_up()
        #self.trail_display.on_touch_up()

    def cast_spell(self, shape):
        if shape:
            self.display.health.on_hit(1/8.0)

    # needed to check if for pass gems (ie, went past the slop window)
    def on_update(self):
        self.audio_ctrl.on_update()

        # check if there are passed gems
        t = self.display.time
        idx=None
        hits = self.song.get_gems_in_range(t-.21, t-.11) #to account for the fact humans are generally early?
        for h in hits:
            idx = self.song.get_gem_index(h)
            if self.display.gems[idx].here:
                self.display.gem_pass(idx)
                self.trail_display.on_miss()

                # mute until note is hit again
                #self.audio_ctrl.set_mute(True)

                # reset score mechanics
                self.streak = 0
                self.bonus = 1

run(MainWidget)
