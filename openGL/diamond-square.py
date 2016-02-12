from random import uniform as random
import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def step(n, rand_max, points):
    rs = [random(-rand_max, rand_max) for i in range(5)]
    glBegin(GL_LINES)
    index = 0
    for i in [[0, n/2], [n/2, 0], [n/2, n], [n, n/2]]:
        glVertex(n/2, rs[0], n/2)
        glVertex(i[0], rs[index], i[1])
        points.append([i[0], rs[index], i[1]])
        index += 1
    glEnd()
    return points

points = []
rand_max = 500
n = 1000
original = 1000

display = (600, 600)
top = 1000
render = 1000
zoom = 1

middle = (top/zoom)/tan(pi/8)

pygame.init()
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), middle-render/zoom, middle+render/zoom)
glTranslate(0, 0, -middle)
glClear(GL_COLOR_BUFFER_BIT)
glTranslate(-500, 0, 0)
k = 1
glRotate(22, 1, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                glRotate(12.25, 1, 0, 0)
            if event.key == pygame.K_UP:
                glRotate(-12.25, 1, 0, 0)
            if event.key == pygame.K_LEFT:
                glRotate(12.25, 0, 1, 0)
            if event.key == pygame.K_RIGHT:
                glRotate(-12.25, 0, 1, 0)

    if k == 5:
        continue
    i = 0
    while i < original:
        glPushMatrix()
        glTranslate(i, 0, 0)
        j = 0
        while j < original:
            glPushMatrix()
            glTranslate(0, 0, j)
            points = step(n, rand_max, points)
            glPopMatrix()
            j += n
        glPopMatrix()
        i += n
    n /= 2
    rand_max /= 1.5

    pygame.display.flip()
    k += 1
