import pygame, math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


zoom = 0.6
top = 11.0
render = 2.0
inc = 2
sp = gluNewQuadric()

pygame.init()
display = (600, 600)

pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

mid = (top/zoom)/math.tan(math.pi/8)
gluPerspective(45, (display[0]/display[1]), mid-render/zoom, mid+render/zoom)
glClear(GL_COLOR_BUFFER_BIT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.display.quit()
            quit()
    theta = 0
    while theta < 2*math.pi:
        glPushMatrix()

        glTranslate(10*math.cos(theta), 10*math.sin(theta), 0)
        gluSphere(sp, 1, 10, 10)
        glPopMatrix()

        theta += math.pi/inc
    inc *= 2
    pygame.display.flip()
