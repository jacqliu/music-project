## Controls the player interactive part and logic that determines which shape is made and what to display and what response to give (probably in on_update...)

from kivy.clock import Clock as kivyClock
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Rectangle, Ellipse, Color, Fbo, ClearBuffers, ClearColor, Line
from kivy.graphics import PushMatrix, PopMatrix, Scale, Callback
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.core.window import Window

import numpy as np
from gfxutil import *

gold = (.1,1,1) #not actually gold right now.

class TrailDisplay(InstructionGroup):
    def __init__(self): #callback function takes in which shape was created
        super(TrailDisplay, self).__init__()
        self.callback = None
        self.timer_push = 1000
        self.timer_miss = 1000
        self.color = Color(hsv=gold) #base color of every node
        self.add(self.color)

        self.objs = []
        self.waste_objs = [] #not certain how many this holds...
        self.waste_objs_x = [] #just for the second one in x's

        self.shapes = {'triangle': 0, 'square': 0, 'diamond': 0, 'x': 0, 'circle': 0}


    def on_touch_down(self, pos, push):
        if not push:
            self.timer_miss = 100
            self.timer_push = 100
            new = CEllipse(cpos = pos, size = (30, 30), segments = 40)
            self.add(new)
            #self.objects.add(new)
            self.objs.append(new)
        else:
            self.timer_push = .2
            if self.objs and len(self.waste_objs_x) == 0 and len(self.waste_objs) == 0: #len 2 is special case for X
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

            else:
                print 'pushed without objects'

            #categorize shapes
            shape = self.possible_types_object()
            if shape:
                self.shapes[shape] += 1
                self.callback(shape)
            else:
                self.on_miss()
            print shape

            if shape == 'triangle':
                self.color.h, self.color.s, self.color.v = (1./3, 1,1) #green
            elif shape == 'square':
                self.color.h, self.color.s, self.color.v = (2./3, 1,1) #blue
            elif shape == 'diamond':
                self.color.h, self.color.s, self.color.v = (.5, 1,1) #light blue
            elif shape == 'circle':
                self.color.h, self.color.s, self.color.v = (.9, 1,1) #magenta
            elif shape == 'x':
                self.color.h, self.color.s, self.color.v = (.5, 1,1)


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
        self.color.h, self.color.s, self.color.v = (0, 1, 1)
        self.timer_miss = .15

    def on_update(self, dt):
        self.timer_push -= dt
        self.timer_miss -= dt
        if self.timer_push < 0 or self.timer_miss < 0:
            ####### CLEAR OBJECTS SUPER IMPORTANT ########
            for o in (self.objs+self.waste_objs+self.waste_objs_x):
                self.remove(o)
            self.objs = []
            self.waste_objs = []
            self.waste_objs_x = []
            self.color.h, self.color.s, self.color.v = gold

    def possible_types_object(self):
        #X detection
        if len(self.objs) == 2 and len(self.waste_objs_x) > 0:
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
            # print p1, p2, p3, p4
            # if self.on_the_same_axis(p1, p2) and ((p1[0] < p2[0] and p3[0] > p4[0]) or (p1[0] > p2[0] and p3[0] < p4[0])): #and self.on_the_same_axis(p2, p3) and self.on_the_same_axis(p4, p1):
            #     return 'x'

        #circle detection
        elif len(self.objs) == 1 and len(self.waste_objs) > 0 and len(self.waste_objs_x) == 0: #idk why it equals 2 but...
            if pt_distance(self.waste_objs[-1].cpos, self.objs[0].cpos) < 30:
                return 'circle'

        #equilateral triangle detection
        elif len(self.objs) == 6:
            points = []
            for i in range(3):
                points.append(self.objs[i].cpos)
            if self.close_enough(points, 1.4):
                return 'triangle'

        #square or diamond detection
        elif len(self.objs) == 8:
            points = []
            for i in range(4):
                points.append(self.objs[i].cpos)
            if self.close_enough(points, 1.8):
                p1 = self.objs[0].cpos
                p2 = self.objs[1].cpos
                p3 = self.objs[2].cpos
                p4 = self.objs[3].cpos
                #if not self.intersect(p1, p2, p3, p4): #and not self.intersect(p3, p4, p1, p2) and not self.intersect(p1, p4, p2, p3) and not self.intersect(p2, p3, p1, p4):
                # numer = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p4[1] + p4[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p4[0]*p3[1] + p1[0]*p4[1])
                # area = abs(numer/2.0)
                # perimeter = pt_distance(p1, p2) + pt_distance(p2, p3) + pt_distance(p3, p4) + pt_distance(p4, p1)
                # print area/perimeter, area, perimeter
                # print "here"
            # if area/perimeter > 10:
                if self.on_the_same_axis(p1, p2) and self.on_the_same_axis(p2, p3) and self.on_the_same_axis(p3, p4) and self.on_the_same_axis(p4, p1):
                    return 'square'
                elif self.on_the_same_axis(p1, p3) and self.on_the_same_axis(p2, p4) and not self.on_the_same_axis(p1, p2) and not self.on_the_same_axis(p3, p4):
                    return 'diamond'


                

    #checks every point in order of creation to make sure they're close enough to each other
    def close_enough(self, points, ratio): #ratio is float
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

    def on_the_same_axis(self, p1, p2):
        ratio = pt_distance(p1, p2)/4.0
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

class Node(InstructionGroup):
    def __init__(self, pos):
        super(Node, self).__init__()
        self.pos = pos
        self.circle = CEllipse(cpos = pos, size = (30, 30), segments = 40)
        self.add(self.circle)

        self.disappear = False

    def on_update(self, dt):
        if self.disappear:
            return False

class TrailLine(InstructionGroup):
    def __init__(self, pts):
        super(TrailLine, self).__init__()
        self.points = pts
        self.line = Line(points=self.points)
        self.add(self.line)

        self.disappear = False

    def on_update(self, dt):
        if self.disappear:
            return False