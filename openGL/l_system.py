from math import * 
import numpy as np
import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import uniform as R

class LSystem():
    def __init__(self, axiom, productions):
        self.word= axiom
        self.rules = productions
        for rule in self.rules:
            if type(self.rules[rule]) == list:
                new_rule = []
                for item in self.rules[rule]:
                    for i in range(item[1]):
                        new_rule.append(item[0])
                self.rules[rule] = new_rule

    def rewrite(self):
        brackets = [s for s in range(len(self.word)) if self.word[s] == ')' or self.word[s] == '(']
        inputs = [(self.word[brackets[i]-1], self.word[brackets[i]+1:brackets[i+1]]) for i in range(0, len(brackets), 2)]
        new_string = []
        
        for inp in inputs:
            if inp[0] in self.rules:
                new_string.extend([i if i != 't' else inp[1] for i in self.rules[inp[0]]])
            else:
                new_string.extend(list(inp[0]+'('+inp[1]+')'))
        
        for index in range(len(self.word)):
            symbol = self.word[index]
            if symbol in '[]':
                new_string.insert(index, symbol)

        new_string = ''.join(new_string)

        self.word = self.clean_word(new_string)

    def clean_word(self, string):
        brackets = [s for s in range(len(string)) if string[s] == ')' or string[s] == '(']
        eval_string = ''
        prev = 0
        for i in range(0, len(brackets), 2):
            eval_string += string[prev:brackets[i]+1]
            eval_string += str(eval(string[brackets[i]+1:brackets[i+1]]))
            prev = brackets[i+1]
        return eval_string+string[brackets[-1]:]

class Turtle():
    def __init__(self, position=[0, 0, 0], head=[1, 0, 0]):
        self.head = np.matrix(head)
        self.head_init = self.head
        self.position = np.matrix(position)
        self.position_init = self.position
        self.moves = []

    def Ru(self, alpha):
        self.head = self.head*np.matrix([[cos(alpha), sin(alpha), 0], [-sin(alpha), cos(alpha), 0], [0, 0, 1]])

    def Rl(self, alpha):
        self.head = self.head*np.matrix([[cos(alpha), 0, -sin(alpha)], [0, 1, 0], [sin(alpha), 0, cos(alpha)]])

    def Rh(self, alpha):
        self.head = self.head*np.matrix([[1, 0, 0], [0, cos(alpha), -sin(alpha)], [0, sin(alpha), cos(alpha)]])

    def reader(self, string):
        self.position = self.position_init
        self.head = self.head_init
        stack = []
        index = 0
        for symbol in string:
            if symbol == '+':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Ru(eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Ru(pi/2)
            elif symbol == '-':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Ru(-eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Ru(-pi/2)
            elif symbol == '&':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Rl(eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Rl(pi/2)
            elif symbol == '^':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Rl(-eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Rl(-pi/2)
            elif symbol == '\\':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Rh(eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Rh(pi/2)
            elif symbol == '/':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    self.Rh(-eval(string[open_bracket+1:closed_bracket]))
                else:
                    self.Rh(-pi/2)
            elif symbol == '|':
                self.Ru(pi)
            elif symbol == '[':
                stack.append((self.position, self.head))
            elif symbol == ']':
                top = stack.pop()
                self.position = top[0]
                self.head = top[1]
            elif symbol == 'F' or symbol == 'R' or symbol == 'L' or symbol == 'G':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    d = eval(string[open_bracket+1:closed_bracket])
                    new_position = self.position + d * self.head
                    self.moves.append((self.position, new_position, 'draw')) 
                    self.position = new_position
                else:
                    new_position = self.position + self.head
                    self.moves.append((self.position, new_position, 'draw')) 
                    self.position = new_position
            elif symbol == 'f' or symbol == 'g':
                if string[index+1] == '(':
                    open_bracket = index+1
                    closed_bracket = string[open_bracket:].find(')')+open_bracket
                    d = eval(string[open_bracket+1:closed_bracket])
                    new_position = self.position + d * self.head
                    self.moves.append((self.position, new_position, 'no draw')) 
                    self.position = new_position
                else:
                    new_position = self.position + self.head
                    self.moves.append((self.position, new_position, 'no draw')) 
                    self.position = new_position
            index += 1

class Graphics():
    def __init__(self, display, top, render, tutle, l_sys, zoom=1.0):
        self.display = display
        self.zoom = zoom
        self.top = top
        self.render = render
        self.turtle = turtle
        self.l_sys = l_sys

        mid = (top/zoom)/tan(pi/8)

        pygame.init()
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), mid-render/zoom, mid+render/zoom)
        glTranslate(0, 0, -mid)

    def draw(self):
        self.turtle.reader(self.l_sys.word)
        for movement in self.turtle.moves:
            position1 = movement[0]
            position2 = movement[1]
            if movement[2] == 'draw':
                glBegin(GL_LINES) 
                glVertex3f(position1.item(0), position1.item(1), position1.item(2))
                glVertex3f(position2.item(0), position2.item(1), position2.item(2))
                glEnd()
            pygame.display.flip()

##CONFIGURE TURTLE:
turtle = Turtle([0, 0, 0])

##CONFIGURE L_SYSTEM:

#islands = LSystem('F+F+F+F', {'f': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF', 'F': 'ffffff'})
#plant = LSystem('F', ls)
#plant2 = LSystem('X(1)', {'X(s)': 'F(s)-(0.4)[[X(s)]+(0.4)X(s)]', 'F(d)': 'F(d)[+(0.4)F(d)]F(d)[-(0.4)F(d)]F(d)'})
d = 1
a = pi/2
koch = LSystem('F(d)-(2*a)F(d)-(2*a)F(d)-(2*a)F(d)-(2*a)F(d)-(2*a)F(d)', {'F': 'F(t/3)+(a)F(t/3)-(2*a)F(t/3)+(a)F(t/3)'})
dragon = LSystem('L(d)', {'L': 'L(d)+(pi/2)R(d)+(pi/2)', 'R': '-(pi/2)L(d)-(pi/2)R(d)'})
#ken = LSystem('G(d)F(d)G(d)', {'G': '[+(a)G(t/6)F(t/6)G(t/6)-(a)]'})
l_sys = dragon

##CONFIGURE GRAPHICS:

gpu = Graphics((600, 600), 100, 1, turtle, l_sys)

for n in range(11):
    gpu.l_sys.rewrite()
    print(gpu.l_sys.word)
while True:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    gpu.turtle.reader(gpu.l_sys.word)
    for movement in gpu.turtle.moves:
        position1 = movement[0]
        position2 = movement[1]
        if movement[2] == 'draw':
            glBegin(GL_LINES) 
            glVertex3f(position1.item(0), position1.item(1), position1.item(2))
            glVertex3f(position2.item(0), position2.item(1), position2.item(2))
            glEnd()
    pygame.display.flip()
    gpu.turtle.moves = []
