from engine import *
import pygame, surfaces
import time

from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

################CONFIGURABLE STUFF##################
fps_count = False
show_springs = True
pinmap = False
spheres = False 

time_step = 1.0/50
zoom = 0.25
display = (600, 600)
####################################################

#PASS THIS IN FROM OTHER FILE#
######################
c = 0.5
struc_k = 3
shear_k = struc_k
bend_k = 5
total = []

fabric = surfaces.cloth(10, struc_k, shear_k, bend_k, c, 1, 0.1)
objects = fabric[0]
springs = fabric[1]

methods = {'down grav': 1}
########################

sim = Simulate(time_step, objects, springs, methods)
clock = pygame.time.Clock()

alpha, theta = 0, 0
sp = gluNewQuadric()

top = max([max(obj.pos[:-1])+obj.r for obj in sim.objects])
render = max([obj.pos[-1]+obj.r for obj in sim.objects])
render = 10

mid = (top/zoom)/tan(pi/8)

pygame.init()
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), mid-render/zoom, mid+render/zoom)
glTranslate(0, 0, -mid)
glClear(GL_COLOR_BUFFER_BIT)
gluQuadricDrawStyle(sp, GLU_FILL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                glTranslate(0, 0, -10)
            if event.key == pygame.K_w:
                glTranslate(0, 0, 10)
            if event.key == pygame.K_e:
                glTranslate(0, 10, 0)
            if event.key == pygame.K_q:
                glTranslate(0, -10, 0)
            if event.key == pygame.K_d:
                glTranslate(-10, 0, 0)
            if event.key == pygame.K_a:
                glTranslate(10, 0, 0)
            if event.key == pygame.K_DOWN:
                glRotate(12.25, 1, 0, 0)
                sim.alpha += pi/16
            if event.key == pygame.K_UP:
                glRotate(-12.25, 1, 0, 0)
                sim.alpha -= pi/16
            if event.key == pygame.K_LEFT:
                glRotate(12.25, 0, 1, 0)
                sim.theta += pi/16
            if event.key == pygame.K_RIGHT:
                glRotate(-12.25, 0, 1, 0)
                sim.theta -= pi/16

#    mousepos = pygame.mouse.get_pos()
#    sim.mousepos = [(mousepos[0]-display[0]/2)*(top/zoom)/display[0], (display[1]/2-mousepos[1])*(top/zoom)/display[1]]
#
    sim.forces()
    sim.integrate()

    if pinmap:
        glBegin(GL_POINTS)
        for p in sim.objects:
            glVertex3f(p.pos[0], p.pos[1], p.pos[2])
        glEnd()


    if spheres:
        for p in sim.objects:
            glPushMatrix()
            glTranslate(p.pos[0], p.pos[1], p.pos[2])
            gluSphere(sp, p.r, 6, 6)
            glPopMatrix()

    if show_springs:
        for connection in sim.connections:
            glBegin(GL_LINES)
            glVertex3f(connection[0].pos[0], connection[0].pos[1], connection[0].pos[2])
            glVertex3f(connection[1].pos[0], connection[1].pos[1], connection[1].pos[2])
            glEnd()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    clock.tick()
    
    if fps_count:
       print(round(clock.get_fps()))
