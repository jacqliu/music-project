########## Additional displays especially for SpellBinder ###########

import sys
sys.path.append('..')
from common.core import *
from common.gfxutil import *

from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.image import Image

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