########## Additional displays especially for SpellBinder ###########

import sys
sys.path.append('..')
from common.core import *
from common.gfxutil import *

from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.image import Image

circle_source = "circle_spell.png"

heart_path = "particle/heart.png"
circle_path = 'particle/circle.png'
square_path = 'particle/square.png'
triangle_path = 'particle/triangle.png'
diamond_path = 'particle/diamond.png'
x_path = 'particle/x.png'

#Only for displaying Background images! Not interactive!
class BGWidget(BaseWidget):
    def __init__(self, bg_source, levels = None):
        super(BGWidget, self).__init__()
     	self.bg = Rectangle(pos=(0, 0), size=(Window.width, Window.height), source = bg_source)
        self.canvas.add(self.bg)

        if levels:
            for i in range(len(levels)): 
                p = (i*Window.width/len(levels), 0)
                s = (Window.width/len(levels), Window.height/3.0)
                c = Color(hsv = gray)
                c.a = .7
                self.canvas.add(c)
                self.canvas.add(Rectangle(pos=p, size=s, source= levels[i][2]))
     	
    def on_update(self):
    	pass

#For displaying health and anything related to the progress of the game. Updates with score.
class HealthDisplay(InstructionGroup):
    def __init__(self, triangles = 0, squares = 0, diamonds = 0, xs = 0, circles = 0):
        super(HealthDisplay, self).__init__()
        self.progress_made = 0
        self.total_progress = 100.0
        self.damage_left = 100.0
        self.total_damage = 100.0
        # self.shapes = [Rectangle(pos=pos, size=(Window.height/4, Window.height/4), source = "../")]

        health_bar_width = 15
        #health bar display
        self.progress_bar = Line(points = [0, Window.height-30, Window.width*self.progress_made/self.total_progress, Window.height-30], width = health_bar_width, cap = 'none')
        self.damage_bar = Line(points = [0, Window.height-60, Window.width*self.damage_left/self.total_damage, Window.height-60], width = health_bar_width, cap = 'none')
        self.add(Color(hsv = gray))
        self.add(self.progress_bar)
        self.add(Color(hsv = lime))
        self.add(self.damage_bar)

        #progress displayp
        # if triangles != 0:
        #     shape = Rectangle(pos=, size=(Window.height/4, Window.height/4), source = circle_path)
            

    def on_miss(self, frac):
        self.damage_left -= self.total_damage*frac
        self.damage_bar.points = [0, Window.height-60, Window.width*self.damage_left/self.total_damage, Window.height-60]

    def on_hit(self, frac, shape):
        self.progress_made += self.total_progress*frac
        self.progress_bar.points = [0, Window.height-30, Window.width*self.progress_made/self.total_progress, Window.height-30]

        # print self.progress_made
        # print frac

    # def on_gain(self, frac, shape):
    #     self.progress_made += self.progress_made*frac
    #     self.progress_bar.points = [0, Window.height, Window.width*self.progress_made/self.total_progress, Window.height]
    #     self.damage_bar.points = [0, Window.height-60, Window.width*self.damage_left/self.total_damage, Window.height-60]

#For any display related to the movement of the cursor.
class CursorDisplay(InstructionGroup):
    def __init__(self):
        super(CursorDisplay, self).__init__()
        self.pos = (0, 0)
        self.cursor = CEllipse(cpos = self.pos, size = (15, 15), segments = 40)
        self.color = Color(hsv = gold)

        self.add(self.color)
        self.add(self.cursor)

        #additional cursor animations
        self.sparkles = []

    def on_update(self, dt):
        # for i in range(int(self.cursor.cpos[0]), int(self.pos[0])): #just a random sparkle generator
        #     sparkle = Spell(CEllipse(cpos = (i, random.randint(self.cursor.cpos[1], self.pos[1])), size = (3, 3), segments = 40))
        #     self.add(sparkle)
        # for s in self.sparkles:
        #     if s.on_update(dt) == False:
        #         self.remove(s)

        self.cursor.cpos = self.pos

#controls all Spell animations, including what should happen per shape made
class SpellDisplay(InstructionGroup):
    def __init__(self):
        super(SpellDisplay, self).__init__()
        self.shapes = {'triangle': self.make_triangle, 'square': self.make_square, 'diamond': self.make_diamond, 'x': self.make_x, 'circle': self.make_circle}
        self.spells = []

    def make_spell(self, shape, nodes):
        shape_obj, color = self.shapes[shape](self.find_center(nodes))
        spell = Spell(shape_obj, color)
        self.add(spell)
        self.spells.append(spell)

    def make_circle(self, pos):
        return (CRectangle(cpos=pos, size=(Window.height/4, Window.height/4), source = circle_source), color_map['c'])

    def make_square(self, pos):
        return (CEllipse(cpos = pos, size = (60, 60), segments = 40), color_map['s'])

    def make_diamond(self, pos):
        return (CEllipse(cpos = pos, size = (60, 60), segments = 40), color_map['d'])

    def make_x(self, pos):
        return (CEllipse(cpos = pos, size = (60, 60), segments = 40), color_map['x'])

    def make_triangle(self, pos):
        return (CEllipse(cpos = pos, size = (60, 60), segments = 40), color_map['t'])

    def on_update(self, dt):
        to_remove = []
        for s in self.spells:
            if s.on_update(dt) == False:
                to_remove.append(s)
        for s in to_remove:
            self.spells.remove(s)

    def find_center(self, nodes):
        x = 0
        y = 0
        for node in nodes:
            x += node.pos[0]
            y += node.pos[1]
        return (x/float(len(nodes)), y/float(len(nodes)))


#a single Spell animation that has shape, color, and duration
class Spell(InstructionGroup):
    def __init__(self, shape, color = gold, duration = 1):#defaults to gold
        super(Spell, self).__init__()
        self.shape = shape
        self.color = Color(hsv = color) 
        self.add(self.color)
        self.add(self.shape)

        self.duration = duration
        self.fade_anim = KFAnim((0, 1), (self.duration, 0))
        self.time = 0

    def on_update(self, dt):
        self.time += dt
        self.color.a = self.fade_anim.eval(self.time)
        if self.time > self.duration:
            return False
        return True




