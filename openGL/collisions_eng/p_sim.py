import math, pygame, time
from shapes import *

from random import uniform as random

from pygame.locals import *
from collisions_eng import *

from OpenGL.GL import *
from OpenGL.GLU import *


class p_sim:
    def __init__(self, fl):

        pygame.init()
        self.display = (700, 700)
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)

        varis = ['G', 'timestep', 'time', 'mode', 'grav', 'cube', 'coll', 'trail', 'zoom', 'render', 'top', 'xbound', 'ybound', 'zbound', 'bodies', 'mass', 'dis', 'vel', 'radii'] 
        varis_new = [0 for i in range(len(varis))]

        fl = open(fl, 'r')
        
        for line in fl.readlines():
            if '//' in line:
                continue

            for index in range(len(varis)):
                var = varis[index]
                if var in line:
                    try:
                        varis_new[index] = float(line[line.index(var)+len(var)+1:])
                    except ValueError:
                        varis_new[index] = str(line[line.index(var)+len(var)+1:])
                        
        G = varis_new[0]
        dt = varis_new[1]
        t = varis_new[2]

        mode = varis_new[3]
        grav = varis_new[4]
        cube_ = varis_new[5]
        coll = varis_new[6]

        self.trail = varis_new[7]

        zoom = varis_new[8]
        render = varis_new[9]
        top = varis_new[10]

        bounds = varis_new[11:14]

        self.bodies = int(varis_new[14])

        self.m = varis_new[15]
        self.r = varis_new[16]
        self.v = varis_new[17]
        self.radius = varis_new[18]


        methods = []
        if 'true' in grav:
            methods.append('grav')
        if 'true' in coll:
            methods.append('coll')
        if 'true' in cube_:
            methods.append('cube')

        alpha = math.pi/8

        self.planets = [Object(100, [0, 0, 0], [0, 0, 0], 1), Object(10, [100, 0, 0], [0, 1, 0], 1)]
        self.points = []

        if 'random' in mode:
            self.random()
        if 'ring' in mode:
            self.ring()

        self.solar_sys = Universe(G, dt, methods, bounds, t)

        mid = (top/(zoom))/math.tan(alpha)
        self.c = cube([0, 0, 0], [2*bound for bound in bounds])

        gluPerspective(45, (self.display[0]/self.display[1]), mid-render, mid+render)
        glTranslate(0, 0, -mid)


    def random(self):
        for p in range(self.bodies):
            self.planets.append(Object(self.m, [random(-self.r, self.r) for i in range(3)], [random(-self.v, self.v) for i in range(3)], self.radius))


    def ring(self):
        theta = 0
        while theta < 2*math.pi:
            self.planets.append(Object(self.m, [self.r*math.cos(theta), self.r*math.sin(theta), 0], [self.v*math.cos(theta+math.pi/2), self.v*math.sin(theta+math.pi/2), 0], self.radius))
            print([self.r*math.cos(theta), self.r*math.sin(theta), 0])
            theta += 2*math.pi/self.bodies

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    glTranslate(0, 0, -10)
                if event.key == pygame.K_w:
                    glTranslate(0, 0, 10)
                if event.key == pygame.K_d:
                    glTranslate(-10, 0, 0)
                if event.key == pygame.K_a:
                    glTranslate(10, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotate(1, 90, 0, 0)
                if event.key == pygame.K_UP:
                    glRotate(1, -90, 0, 0)
                if event.key == pygame.K_LEFT:
                    glRotate(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotate(1, 0, -1, 0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        if 'false' in self.trail:
            for p in self.planets:
                glPushMatrix()
                glTranslate(p.s[0], p.s[1], p.s[2])
                gluSphere(gluNewQuadric(), p.r, 10, 10)
                glPopMatrix()

        else:
            for p in self.planets:
                self.points.append([[p.s[0], p.s[1], p.s[2]], p.r])

        for p in self.c:
            glBegin(GL_LINES)
            glVertex(p[0][0], p[0][1], p[0][2])
            glVertex(p[1][0], p[1][1], p[1][2])
            glEnd()

        pygame.display.flip()
        self.planets = self.solar_sys.time_step(self.planets)


new = p_sim('fl')
while True:
    new.draw()

#    glRotate(1, 0, 1, 0)
