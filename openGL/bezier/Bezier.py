import math, pygame
from random import uniform as R

import numpy as np
from sympy import * 

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def compare(points, inc):
    total = [[], []]

    n = len(points)-1
    t = symbols('t')
    t_inc = 0
    equs = np.array([0, 0, 0])

    for i in range(len(points)):
        equs = equs + points[i]*((factorial(n)/(factorial(i)*factorial(n-i)) * t**i * (1-t)**(n-i)))
    
    while t_inc <= 1.0:
        total[0].append(np.array([equ.subs(t, t_inc) for equ in equs]))
        total[1].append(bezier(points, t_inc))

        t_inc += inc

    return total

def bezier(points, t):
    if len(points) == 1:
        return points[0]

    return bezier([(1-t)*points[p] + t*points[p+1] for p in range(len(points)-1)], t)

def main():

    zoom = 1.0
    top = 100.0
    render = 155.0
    sp = gluNewQuadric()

    mid = (top/zoom)/math.tan(math.pi/8)

    points = [[np.array([R(-top, top), R(-top, top), R(-top, top)]) for i in range(10)] for i in range(10)]
    inc = 0.005
    total2 = []
    
    for i in points:
        total2.append(compare(i, inc))

    n = len(points)-1

    pygame.init()

    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), mid-render, mid+render)
    glTranslate(0, 0, -mid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    glTranslate(0, 0, -10)
                    pygame.display.flip()
                if event.key == pygame.K_w:
                    glTranslate(0, 0, 10)
                if event.key == pygame.K_d:
                    glTranslate(-10, 0, 0)
                if event.key == pygame.K_a:
                    glTranslate(10, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotate(1, 1, 0, 0)
                if event.key == pygame.K_UP:
                    glRotate(1, -1, 0, 0)
                if event.key == pygame.K_LEFT:
                    glRotate(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotate(1, 0, -1, 0)

        glClear(GL_COLOR_BUFFER_BIT)

        for total in total2:
            for index in range(len(total[0])-1):
                p = total[0][index]
                p2 = total[0][index+1]
                glBegin(GL_LINES)
                glVertex3f(p[0], p[1], p[2])
                glVertex3f(p2[0], p2[1], p2[2])
                glEnd()

                glPushMatrix()
                glTranslate(p[0], p[1], p[2])
                gluSphere(sp, 1, 4, 4)
                glPopMatrix()
    
        for k in points:
            for p in k:
                glPushMatrix()
                glTranslate(p[0], p[1], p[2])
                gluSphere(sp, 2, 10, 10)
                glPopMatrix()

        pygame.display.flip()

main()
