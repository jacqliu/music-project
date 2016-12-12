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
from trail import *
from displays import *

from kivy.graphics.instructions import InstructionGroup, VertexInstruction
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.graphics import PushMatrix, PopMatrix, Translate, Scale, Rotate
from kivy.clock import Clock as kivyClock
from common.kivyparticle import ParticleSystem

import random
import numpy as np
import bisect
import zmq
import zlib
import pickle

from kivy.core.image import Image

# appropriate files
traverse_town = ("../../kh_traverse_town.wav", "../../kh_traverse_town_gems.txt", "../../traverse_bg.jpg", "Traverse Town - Kingdom Hearts")
mirror_mirror = ("../../mirror_mirror.wav", "../../mirror_mirror_gems.txt", "../../mirror_bg.jpg", "Mirror Mirror - RWBY")
xion = ("../../xion.wav", "../../xion.txt", "../../xion_bg.jpg", "Xion's Theme - Kingdom Hearts")
canon = ("../../canon.wav", "../../canon_gems.txt", "../../canon_bg.jpg", "Pachelbel's Canon")
levels = [traverse_town, mirror_mirror, xion, canon]
# takemeout_solo = "../../TakeMeOut_solo.wav"
tmo_sfx = "../../sfx.txt"
# wav_file = "../../mirror_mirror.wav"
# wav_file = "../../xion.wav"
#wav_file = "../../kh_traverse_town.wav"
# gems_path = "../../mirror_mirror_gems.txt"
# gems_path = "../../xion.txt"
#gems_path = "../../kh_traverse_town_gems.txt"
barline_path = "../../mirror_mirror_gems.txt"
start_bg = "../../start_screen.jpg"
#bg_source = "../../background.png"
# bg_source = "../../landscape.jpg"

MOVE_BUTTON_VAL = 128 #524288
TRIGGER_VAL = 64 #1048576 
TRIANGLE_VAL = 16

# Set up ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5555")

class MainWidget(BaseWidget) :
    def __init__(self):
        super(MainWidget, self).__init__()
        # keep track of if game is over
        self.dead = False
        
        # audio controller
        self.audioctrl = None
        # background
        self.background = BGWidget(start_bg, levels)
        self.add_widget(self.background)

        # text
        # self.info = topleft_label()
        # self.add_widget(self.info)

        # keep track of objects
        self.objects = None
        # keep track of song and data
        self.song = None
        # particle system
        self.ps = None
        #psmove
        self.data = None
        self.trigger_held = None
        self.press_pos = None
        #trail display - must be before beat match display, otherwise will translate.... lol
        self.trail_display = None
        #cursor display
        self.cursor_display = None
        #make spells
        self.spells = None
        # display
        self.display = None
        # player
        self.player = None

        self.paused = True
        self.playing = False

        #start a level
        #self.start_level(wav_file, gems_path, bg_source)
    def start_screen(self):
        self.dead = False
        self.canvas.clear()
        self.playing = False
        self.paused = True

        self.background = BGWidget(start_bg, levels)
        self.add_widget(self.background)

        # keep track of objects
        self.objects = AnimGroup()
        self.canvas.add(self.objects)

        #cursor display
        self.cursor_display = CursorDisplay()
        self.objects.add(self.cursor_display)

    def start_level(self, wave_file, gems_path, background_img_src):
        #set start variables based on screen size
        global lanes_height, lanes_width, now_bar_width
        lanes_height = Window.height/4 * 3 - 50
        lanes_width = Window.width/2
        now_bar_width = (lanes_height-now_bar_loc)/float(lanes_height)*(bottom_diff-top_diff) + top_diff
        redraw_window()

        self.dead = False
        self.paused = True
        self.end = False
        self.canvas.clear()

        # audio controller
        self.audioctrl = AudioController(wave_file)

        # background
        self.background = BGWidget(background_img_src)
        self.add_widget(self.background)

        # text for scoring
        self.info = topleft_label()
        self.add_widget(self.info)

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

        #psmove
        self.data = [None, None, None]
        self.trigger_held = False
        self.press_pos = None

        #trail display - must be before beat match display, otherwise will translate.... lol
        self.trail_display = TrailDisplay()
        self.objects.add(self.trail_display)

        #cursor display
        self.cursor_display = CursorDisplay()
        self.objects.add(self.cursor_display)

        #make spells
        self.spells = SpellDisplay()
        self.objects.add(self.spells)

        # display
        self.display = BeatMatchDisplay(gem_data, barlines_data, self.ps)
        self.objects.add(self.display)

        # player
        self.player = Player(self.song, self.display, self.audioctrl, self.trail_display, self.spells)

        self.playing = True

    def level_select(self, pos):
        if pos[1] < Window.height/3.0:
            return levels[int(pos[0])*len(levels)/int(Window.width)]


    def on_key_down(self, keycode, modifiers):
        # play / pause toggle
        # pass
        if keycode[1] == 't':
            self.start_level(traverse_town[0], traverse_town[1], traverse_town[2])
        elif keycode[1] == 'x':
            self.start_level(xion[0], xion[1], xion[2])
        elif keycode[1] == 'r':
            self.start_level(mirror_mirror[0], mirror_mirror[1], mirror_mirror[2])
        elif keycode[1] == 'c':
            self.start_level(canon[0], canon[1], canon[2])
        elif keycode[1] == 's':
            self.start_screen()

        if self.playing: #should be able to eventually get rid of this line, or replace with something else
            if keycode[1] == 'p':
                self.paused = not self.paused

            elif keycode[1] == 'm':
                self.player.on_button_down(None, True)


    def on_key_up(self, keycode):
        if keycode[1] == 'm' and self.playing:
            self.player.on_button_up(0)

    #called by psmove
    def ps_on_touch_down(self, pos, move_button_down):
        if self.playing:
            self.player.on_button_down(pos, move_button_down)

    def ps_on_touch_move(self, pos):
        if self.playing:
            self.player.on_trigger_hold(pos)

    def ps_on_touch_up(self, pos):
        if self.playing:
            self.player.on_button_up(pos)
        else:
            lvl = self.level_select(touch.pos)
            self.start_level(lvl[0], lvl[1], lvl[2])

    #called by normal mouse and keyboard control
    def on_touch_down(self, touch):
        if self.playing:
            self.player.on_button_down(touch.pos, False)

    def on_touch_move(self, touch):
        if self.playing:
            self.player.on_trigger_hold(touch.pos)

    def on_touch_up(self, touch):
        if self.playing:
            self.player.on_button_up(touch.pos)
        else:
            lvl = self.level_select(touch.pos)
            self.start_level(lvl[0], lvl[1], lvl[2])
        
    def on_update(self):
        #getting data form psmove. Trigger presses and releases are events, otherwise vals will be [0, 0].
        if self.playing:
            try:
                # Check for a message, this will not block
                z = socket.recv(flags=zmq.NOBLOCK)
                p = zlib.decompress(z)
                (vals, [x, y], radius) = pickle.loads(p) #data from test.py
                
                #print "Message received:", pickle.loads(p)

                #normalize x and y
                if y > 500: #y actually has an upper and lower bound
                    y = 500
                x = x/600.0
                y = (500-y)/500.0 #reverse direction
                pos = [x*Window.height + 100, y*Window.height] #so technically there is a bounding box... but if x exceeds expectations, that's ok too  
                #print pos

                #update cursor location
                self.cursor_display.pos = pos

                #button action control
                if vals[0] == TRIGGER_VAL: #press down trigger
                    self.ps_on_touch_down(pos, False)
                    self.trigger_held = True
                    self.press_pos = pos
                elif vals[1] == TRIGGER_VAL:
                    self.press_pos = None
                    self.trigger_held = False
                        
                elif vals[0] == MOVE_BUTTON_VAL: #press down move button
                    self.ps_on_touch_down(pos, True)

                elif vals[0] == 0:
                    self.ps_on_touch_up(pos)

                elif vals[0] == TRIANGLE_VAL:
                    self.paused = not self.paused

                #decide if trigger was being held
                if self.trigger_held and self.press_pos != None:
                    if pt_distance(pos, self.press_pos) > 60: #threshold for movement to be considered a hold
                        self.ps_on_touch_move(pos)

            except zmq.Again as e:
                pass

            #make sure game isn't over
            if self.display.health.damage_left <= 0:
                self.dead = True

            #display text
            self.info.text = 'Score: '+ str(self.player.score)
            self.info.text += '\nStreak: ' + str(self.player.streak)
            self.info.text += '\nBonus: ' + str(self.player.bonus) + 'x \n\n'
            self.info.text += str(self.trail_display)

            if not self.paused:
                self.player.on_update()
                self.objects.on_update()
            else:
                self.info.text += '\n\nPress triangle to start!'

            #end game screen
            if len(self.audioctrl.mixer.generators) == 0 or self.dead:
                if self.audioctrl.mixer.generators != 0: #premature end
                    self.audioctrl.song.set_gain(0)

                self.canvas.clear()
                l = Label(text = "text", halign='left', valign='middle', font_size='20sp',
                  pos=(Window.width * 0.5, Window.height * 0.4),
                  text_size=(Window.width, Window.height))
                self.add_widget(l)
                l.text ='streak: %d' % self.player.max_streak
                l.text += "\ntotal score: %d" % (self.player.score)
                if len(self.audioctrl.mixer.generators) != 0:
                    l.text += "\nEcho was overwhelmed by the music."


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
            time, note = line.strip().split('\t')
            self.gems.append((time, note))

        # get barlines
        with open(barline_file) as f:
            content = f.readlines()
        for line in content:
            time, note = line.strip().split('\t')
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
    def __init__(self, pos, color, current_time, gem_time):
        super(GemDisplay, self).__init__()

        self.radius_anim = KFAnim((current_time, 0, 0), (gem_time-(lanes_height-now_bar_loc)/float(time_len)-.1, 0, 0), (gem_time-(lanes_height-now_bar_loc)/float(time_len), top_diff*2-10, top_diff*2-10), (gem_time+now_bar_loc/float(time_len), bottom_diff*2, (top_diff*2-10)*3))
        self.time = current_time

        self.pos_anim = KFAnim((current_time, lanes_width, lanes_height), (gem_time-(lanes_height-now_bar_loc)/float(time_len), lanes_width, lanes_height), (gem_time, lanes_width, now_bar_loc), (gem_time+(lanes_height-now_bar_loc)/float(time_len), lanes_width, now_bar_loc-lanes_height))

        # animate radius
        w, h = self.radius_anim.eval(self.time)
        # self.circle.csize = (2*rad, 2*rad)

        # animate position
        pos = self.pos_anim.eval(self.time)
        self.pos = pos

        # self.time = 0

        # self.pos = pos
        self.color = Color(hsv=color)
        self.add(self.color)
        self.gem = CEllipse(cpos = self.pos, size = (w, h), segments = 40)
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

        if self.here:
            # animate radius
            w,h = self.radius_anim.eval(self.time)
            self.gem.csize = (w, h)

            # animate position
            pos = self.pos_anim.eval(self.time)
            self.gem.cpos = pos

        self.time += dt
        if not self.here and self.gem.size != (0,0):
            self.gem.size = (0,0)
            try:
                self.remove(self.gem)
            except:
                pass

        return self.here

# Displays one button on the nowbar
class ButtonDisplay(InstructionGroup):
    def __init__(self, ps):
        super(ButtonDisplay, self).__init__()

        self.ps = ps

    # displays when button is down (and if it hit a gem)
    def on_down(self, hit, coords, ps_start):
        if hit:
            self.ps.emitter_x = lanes_width
            self.ps.emitter_y = now_bar_loc
            if ps_start:
                self.ps.start() #TODO replace with something more editable and useful.

    # back to normal state
    def on_up(self):
        self.ps.stop()

    def on_update(self, dt):
        pass

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
        ## CHANGING
        self.lanes = []
        # for i in range(Window.height-60, Window.height, 30):
        #     line = Line(points=[0, i, Window.width, i])
        #     self.lanes.append(line)
        #     self.add(line)

        line_left = Line(points=[lanes_width-bottom_diff, 0, lanes_width-top_diff, lanes_height])
        self.lanes.append(line_left)
        self.add(line_left)

        line_right = Line(points=[lanes_width+bottom_diff, 0, lanes_width+top_diff, lanes_height])
        self.lanes.append(line_right)
        self.add(line_right)

        ## CHANGING
        # self.now_bar = Line(points=[now_bar_loc, Window.height-60, now_bar_loc, Window.height-30], width=1) #TODO - switch to relative to height of window
        # self.add(self.now_bar)

        self.now_bar = Line(points=[lanes_width-now_bar_width, now_bar_loc, lanes_width+now_bar_width, now_bar_loc])
        self.add(self.now_bar)

        print now_bar_width
        
        # make button for now bar
        self.button = ButtonDisplay(ps)

        #make health bar
        self.health = HealthDisplay(triangles = 5, xs = 3) #TODO replace with some actual metrics from gem_data
        self.add(self.health)

        # set up translation
        self.translate = Translate()
        self.add(self.translate)

        # keep track of shapes and anims
        self.shapes = []

        # make gems and shape cues
        self.shapes_count = 0
        self.gems_raw = gem_data
        self.gems = []
        last_t = 0
        for (t,letter) in self.gems_raw:
            # make gem in correct lane and location
            pos = [float(t)*time_len+now_bar_loc, Window.height-60+15]

            # colors for downbeat
            if letter == 'b':
                c = white
            else:
                c = red
            g = GemDisplay(pos, c, 0, float(t))
            self.gems.append(g)
            self.add(g)

            # indicate suggested shape
            if letter in ['c', 't', 's', 'd', 'x']:
                self.add_shape(letter, pos, float(last_t))
                self.shapes_count += 1

            last_t = t

    def add_shape(self, letter, pos, t):
        shape_map = {'c':circle_path, 't':triangle_path, 's': square_path, 'd': diamond_path, 'x': x_path}
        text = Image(shape_map[letter]).texture

        rad_anim = KFAnim((t-.1, 0), (t, 50), (t+shape_time, 0))
        rad = rad_anim.eval(self.time)
        
        self.add(Color(hsv = color_map[letter])) #set color of thing. Color_map comes from trail.py
        sh = CRectangle(texture=text, cpos=(lanes_width, lanes_height+50), csize=(rad, rad), color=cyan)
        self.add(sh)
        self.add(self.color) #set back to original

        self.shapes.append((sh, rad_anim))

    # called by Player. Causes the right thing to happen
    def gem_hit(self, gem_idx):
        self.gems[gem_idx].on_hit()

    # called by Player. Checks if gem exists and can be hit.
    def gem_here(self, gem_idx):
    	return self.gems[gem_idx].here

    # called by Player. Causes the right thing to happen
    def gem_pass(self, gem_idx):
        self.gems[gem_idx].on_pass()

    # called by Player. Causes the right thing to happen
    def on_button_down(self, hit, coords, ps_start):
        self.button.on_down(hit, coords, ps_start)

    # called by Player. Causes the right thing to happen
    def on_button_up(self):
        self.button.on_up()

    # call every frame to make gems and barlines flow down the screen
    def on_update(self, dt) :
        for g in self.gems:
            g.on_update(dt)
        self.time += dt

        for (sh, anim) in self.shapes:
            rad = anim.eval(self.time)
            sh.csize = (rad, rad)

        # every second is time_len coords height wise
        # self.translate.x = -self.time*time_len


# Handles game logic and keeps score.
# Controls the display and the audio
class Player(object):
    def __init__(self, song, display, audio_ctrl, trail_display, spell_display):
        super(Player, self).__init__()

        self.display = display
        self.trail_display = trail_display
        self.trail_display.callback = self.cast_spell
        self.spells = spell_display

        self.audio_ctrl = audio_ctrl

        self.song = song
        self.gem_data = self.song.get_gems()
        self.barlines_data = self.song.get_barlines()

        # score mechanics
        self.max_streak = 0
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

        if self.streak > 10: #particle system combo mechanic
            self.display.on_button_down(hit, coords, True)
        else:
            self.display.on_button_down(hit, coords, False)

        if hit and self.display.gem_here(idx):
            self.trail_display.on_touch_down(pos, push)

            # start playing solo again if hit
            # self.audio_ctrl.set_mute(False)
            self.display.gem_hit(idx)

            # score mechanics
            self.streak += 1
            # self.score += self.bonus * 100
            self.bonus = self.streak / 10 + 1
            self.max_streak = max(self.streak, self.max_streak)
        else:
            # if hit is in the wrong lane, pass the gem and play sound
            if idx != None:
                self.display.gem_pass(idx)
                #self.audio_ctrl.play_sfx()

            self.trail_display.on_miss()

            # score mechanics, reset streak and bonus
            self.reset_score_mechanics()

    #called by MainWidget
    def on_trigger_hold(self, pos):
        self.trail_display.on_trigger_hold(pos)

    # called by MainWidget
    def on_button_up(self, pos):
        self.display.on_button_up()
        #self.trail_display.on_touch_up()

    #determines how much damage is done
    def cast_spell(self, shape, nodes):
        if shape:
            #modifies health bar
            self.display.shapes_count = max(5, self.display.shapes_count) #so we can play unauthored ones too
            if shape == "miss":
                self.display.health.on_miss(1./len(self.gem_data)) 
            else:
                self.display.health.on_hit(1./self.display.shapes_count, shape)
                #creates spell animation
                self.spells.make_spell(shape, nodes)

            # adjust score
            if shape == "triangle":
                self.score += 300*self.trail_display.shapes[shape]*self.bonus
            elif shape == "circle":
                self.score += 400*self.trail_display.shapes[shape]*self.bonus
            elif shape == "x":
                self.score += 400*self.trail_display.shapes[shape]*self.bonus
            elif shape == "square" or shape == "diamond":
                self.score += 500*self.trail_display.shapes[shape]


    # reset score mechanics if gem is missed
    def reset_score_mechanics(self):
        self.streak = 0
        self.bonus = 1

    # needed to check if for pass gems (ie, went past the slop window)
    def on_update(self):
        self.audio_ctrl.on_update()

        # check if there are passed gems
        t = self.display.time
        idx=None
        hits = self.song.get_gems_in_range(t-.21, t-.11) #to account for the fact humans are generally early?
        for h in hits:
            idx = self.song.get_gem_index(h)
            if self.display.gems[idx].here and not self.display.gems[idx].miss:
                self.display.gem_pass(idx)
                # if self.miss:
                self.trail_display.on_miss()

                # mute until note is hit again
                #self.audio_ctrl.set_mute(True)

                # reset score mechanics
                self.reset_score_mechanics()

run(MainWidget)
