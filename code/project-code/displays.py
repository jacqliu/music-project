########## Additional displays especially for SpellBinder ###########

import sys
sys.path.append('..')
from common.core import *
from common.gfxutil import *

from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.image import Image

circle_source = "circle_spell.png"

class BGWidget(BaseWidget):
    def __init__(self, bg_source):
        super(BGWidget, self).__init__()
     	self.bg = Rectangle(pos=(0, 0), size=(Window.width, Window.height), source = bg_source)
     	self.canvas.add(self.bg)

    def on_update(self):
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

class CursorDisplay(InstructionGroup):
    def __init__(self):
        super(CursorDisplay, self).__init__()
        self.pos = (0, 0)
        self.cursor = CEllipse(cpos = self.pos, size = (15, 15), segments = 40)
        self.color = Color(hsv = gold)

        self.add(self.color)
        self.add(self.cursor)

    def on_update(self, dt):
        self.cursor.cpos = self.pos

class SpellDisplay(InstructionGroup):
    def __init__(self):
        super(SpellDisplay, self).__init__()
        self.shapes = {'triangle': self.make_triangle, 'square': self.make_square, 'diamond': self.make_diamond, 'x': self.make_x, 'circle': self.make_circle}
        self.spells = []

    def make_spell(self, shape, nodes):
        shape_obj, color = self.shapes[shape](nodes[0].pos)
        spell = Spell(shape_obj, color)
        self.add(spell)
        self.spells.append(spell)

    def make_circle(self, pos):
        return (Rectangle(pos=pos, size=(Window.height/4, Window.height/4), source = circle_source), color_map['c'])

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


class Spell(InstructionGroup):
    def __init__(self, shape, color = gold):#defaults to gold
        super(Spell, self).__init__()
        self.shape = shape
        self.color = Color(hsv = color) 
        self.add(self.color)
        self.add(self.shape)

        self.duration = 1
        self.fade_anim = KFAnim((0, 1), (self.duration, 0))
        self.time = 0

    def on_update(self, dt):
        self.time += dt
        self.color.a = self.fade_anim.eval(self.time)
        if self.time > self.duration:
            return False
        return True




