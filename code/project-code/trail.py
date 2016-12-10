## Controls the player interactive part and logic that determines which shape is made and what to display and what response to give (probably in on_update...)

from kivy.clock import Clock as kivyClock
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle, Ellipse, Color, Fbo, ClearBuffers, ClearColor, Line
from kivy.graphics import PushMatrix, PopMatrix, Scale, Callback
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.core.window import Window

import numpy as np
import random
from common.gfxutil import *

class TrailDisplay(InstructionGroup):
    def __init__(self): #callback function takes in which shape was created
        super(TrailDisplay, self).__init__()
        self.callback = None
        # self.timer_push = 1000
        # self.timer_miss = 1000
        self.push = False
        self.miss = False
        self.miss_particle = None
        self.color = Color(hsv=gold) #base color of every node
        self.add(self.color)

        #trail objects
        self.objs = []
        self.waste_objs = [] #not certain how many this holds...
        self.waste_objs_x = [] #just for the second one in x's

        self.spells = []

        self.shapes = {'triangle': 0, 'square': 0, 'diamond': 0, 'x': 0, 'circle': 0}


    def on_touch_down(self, pos, push):
        #draw shapes, game logic
        if not push:
            # self.timer_miss = 100
            # self.timer_push = 100
            self.miss = False
            self.push = False
            new = CEllipse(cpos = pos, size = (30, 30), segments = 40)
            self.add(new)
            self.objs.append(new)
        else:
            #self.timer_push = .2
            self.push = True
            if self.objs and len(self.waste_objs_x) < 5 and len(self.waste_objs) < 5: #len 2 is special case for X
                lines = []
                for i in range(len(self.objs)-1):
                    pos1 = self.objs[i].cpos
                    pos2 = self.objs[i+1].cpos
                    line = Line(points=[pos1[0], pos1[1], pos2[0], pos2[1]])
                    self.add(line)
                    lines.append(line)
                line = Line(points=[self.objs[0].cpos[0], self.objs[0].cpos[1], self.objs[-1].cpos[0], self.objs[-1].cpos[1]])
                self.add(line)
                self.objs += lines + [line]

            # else:
            #     print 'pushed without objects'

            #categorize shapes, callback function to player
            shape = self.possible_types_object()
            if shape:
                self.shapes[shape] += 1
                self.callback(shape, list(self.objs)) #modifies health, can also be used for game logic
            else:
                self.on_miss()
            print shape

    def on_trigger_hold(self, pos):
        #special case for X
        if len(self.objs) == 2:
            new = CEllipse(cpos = pos, size = (10, 10), segments = 40)
            self.add(new)
            self.waste_objs_x.append(new)
        elif len(self.objs) != 0:
            new = CEllipse(cpos = pos, size = (10, 10), segments = 40)
            self.add(new)
            self.waste_objs.append(new)

    def on_miss(self):
        self.color.h, self.color.s, self.color.v = white
        #TODO miss animation. Can't decide
        # if len(self.objs) != 0: #
        #     self.miss_particle = MissParticle(self.objs[0].pos)
        # self.add(self.miss_particle)
        #self.timer_miss = .15
        self.miss = True

    def on_update(self, dt):
        # self.timer_push -= dt
        # self.timer_miss -= dt

        if self.push or self.miss: #self.timer_push < 0 or self.timer_miss < 0:
            ####### CLEAR OBJECTS SUPER IMPORTANT ########
            for o in (self.objs+self.waste_objs+self.waste_objs_x):
                self.remove(o)
            self.objs = []
            self.waste_objs = []
            self.waste_objs_x = []
            self.color.h, self.color.s, self.color.v = gold

        if len(self.objs) > 10 and self.miss == False:
            self.on_miss()

    def possible_types_object(self):
        #circle detection
        if len(self.objs) == 1 and len(self.waste_objs) > 0: #and len(self.waste_objs_x) == 0: #idk why it equals 2 but...
            if pt_distance(self.waste_objs[-1].cpos, self.objs[0].cpos) < 100 and pt_distance(self.waste_objs[len(self.waste_objs)/2].cpos, self.objs[0].cpos) > 200:
                return 'circle'

        #X detection
        elif len(self.objs) == 2 and len(self.waste_objs_x) > 0:
            p1 = self.objs[0].cpos
            p2 = self.objs[1].cpos
            try:
                p3 = self.waste_objs[-1].cpos
                p4 = self.waste_objs_x[-1].cpos
                print p1, p2, p3, p4
                if self.on_the_same_axis(p1, p2) and ((p1[0] < p2[0] and p3[0] > p4[0]) or (p1[0] > p2[0] and p3[0] < p4[0])): #and self.on_the_same_axis(p2, p3) and self.on_the_same_axis(p4, p1):
                    return 'x'
            except:
                pass

        #equilateral triangle detection
        elif len(self.objs) == 6:
            points = []
            for i in range(3):
                points.append(self.objs[i].cpos)
            if self.close_enough(points, 1.5):
                return 'triangle'

        #square or diamond detection
        elif len(self.objs) == 8:
            points = []
            for i in range(4):
                points.append(self.objs[i].cpos)
            if self.close_enough(points, 2):
                p1 = self.objs[0].cpos
                p2 = self.objs[1].cpos
                p3 = self.objs[2].cpos
                p4 = self.objs[3].cpos
                if self.on_the_same_axis(p1, p2) and self.on_the_same_axis(p2, p3) and self.on_the_same_axis(p3, p4) and self.on_the_same_axis(p4, p1):
                    return 'square'
                elif self.on_the_same_axis(p1, p3) and self.on_the_same_axis(p2, p4) and not self.on_the_same_axis(p1, p2, 6.0) and not self.on_the_same_axis(p3, p4, 6.0):
                    return 'diamond'

    #checks every point in order of creation to make sure they're close enough to each other
    def close_enough(self, points, ratio): #smaller ratio requires points to be closer together
        prior_dist = None
        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            distance = pt_distance(p1, p2)
            if prior_dist != None and (distance < prior_dist/ratio or distance > prior_dist*ratio):
                return False
            prior_dist = distance
        distance = pt_distance(points[0], points[-1])
        if prior_dist != None and (distance < prior_dist/ratio or distance > prior_dist*ratio):
            return False

        return True

    def on_the_same_axis(self, p1, p2, ratio = 2.0):
        ratio = pt_distance(p1, p2)/ratio #smaller denominator means user can be more off
        return (abs(p1[0] - p2[0]) < ratio or abs(p1[1] - p2[1]) < ratio)

    #checks if p3 and p4 are on opposite sides of the line drawn by p1 and p2
    def intersect(self, p1, p2, p3, p4): 
        def line_eq(x, y):
            slope = p1[1]-p2[1]/(p1[0] - p2[0] + .0001) #avoid divisions by zero when you're too precise
            print "slope", slope, p1, p2
            return slope*(x - p1[0]) - (y-p1[1])

        print "line_values", line_eq(p3[0], p3[1]), line_eq(p4[0], p4[1]) , line_eq(p3[0], p3[1]), line_eq(p4[0], p4[1])
        if (line_eq(p3[0], p3[1]) > 0 and line_eq(p4[0], p4[1]) < 0) or (line_eq(p3[0], p3[1]) < 0 and line_eq(p4[0], p4[1]) > 0):
            return True
        return False

    def __str__(self):
        new = ""
        for key in self.shapes: 
            new += key + ': ' + str(self.shapes[key]) + '\n'
        return new

class MissParticle(InstructionGroup):
    def __init__(self, pos):
        super(MissParticle, self).__init__()
        self.parts = []
        for i in range(10):
            part = CEllipse(cpos = (random.randint(pos[0]-100, pos[0]+100), random.randint(pos[1]-100, pos[1]+100)), size = (10, 10), segments = 40)
            self.add(part)

        self.disappear = False

    def on_update(self, dt):
        if self.disappear:
            return False