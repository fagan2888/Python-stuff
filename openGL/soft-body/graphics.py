from engine import *
from surfaces import *
import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

clock = pygame.time.Clock()
fps_count = False

c = 0.2
k = 30
r = 2
app_mag = 100
total = []
springs = []
objects = []
cur = 0

for dawg in range(-3, 4):
    points = []
    for i in range(-3, 4):
        point = [10*i, 0, 10*dawg]
        if point not in points:
            points.append(point)

    for z in points:
        if z == points[0] or z == points[-1]:
            objects.append(Object(1, z, [0, 0, 0], False))
        else:
            objects.append(Object(1, z, [0, 10, 1]))

    for j in range(len(points)-1):
        springs.append(Spring(k, c, [j+cur, j+1+cur]))
    total.append(points)
    cur += 7

test = Engine(0.1, objects, springs) 

sp = gluNewQuadric()

alpha, theta = 0, 0

top = 10
zoom = 0.1
render = 50
mid = (top/zoom)/tan(pi/8)

pygame.init()
display = (600, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), mid-render, mid+render)
glTranslate(0, 0, -mid)
glClear(GL_COLOR_BUFFER_BIT)
gluQuadricDrawStyle(sp, GLU_FILL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.display.quit()
            quit()
#FIND A WAY TO PUT THIS IN ENGINE
#        if event.type == pygame.MOUSEBUTTONDOWN:
#            for obj in objects:
#                mousepos = pygame.mouse.get_pos()
#                mousepos = [(mousepos[0]-display[0]/2)*(top/zoom)/display[0], (display[1]/2-mousepos[1])*(top/zoom)/display[1]]
#                if ((mousepos[0]-obj.pos[0])**2 + (mousepos[1]-obj.pos[1])**2)**0.5 <= r:
#                    force.push([app_mag*cos(alpha)*sin(theta), app_mag*-sin(alpha), app_mag*sin(theta)*cos(alpha)])

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
                glRotate(12.25, 1, 0, 0)
                alpha += pi/16
            if event.key == pygame.K_UP:
                glRotate(-12.25, 1, 0, 0)
                alpha -= pi/16
            if event.key == pygame.K_LEFT:
                glRotate(12.25, 0, 1, 0)
                theta += pi/16
            if event.key == pygame.K_RIGHT:
                glRotate(-12.25, 0, 1, 0)
                theta -= pi/16

    mousepos = pygame.mouse.get_pos()
    mousepos = [(mousepos[0]-display[0]/2)*(top/zoom)/display[0], (display[1]/2-mousepos[1])*(top/zoom)/display[1]]

    test.forces(9.8, 0, 0, 0)
    connections = test.spring_sim()
    test.mouse_interact(mousepos, alpha, theta, r, app_mag)
    points = test.integrate()

    for p in points:
        glPushMatrix()
        glTranslate(p[0], p[1], p[2])
        gluSphere(sp, r, 10, 10)
        glPopMatrix()

    for connection in connections:
        glBegin(GL_LINES)
        glVertex3f(connection[0].pos[0], connection[0].pos[1], connection[0].pos[2])
        glVertex3f(connection[1].pos[0], connection[1].pos[1], connection[1].pos[2])
        glEnd()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT)

    clock.tick()
    
    if fps_count:
       print(round(clock.get_fps()))
