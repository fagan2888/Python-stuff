from math import *
import numpy as np
import force

class Object():
    def __init__(self, m, pos, vel, r, dynamic=True):
        self.dynamic = dynamic
        self.m = float(m)
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.forces = np.array([0, 0, 0])
        self.r = r

class Spring():
    def __init__(self, k, c, connect):
        self.connect = connect
        self.k = k
        self.c = c
        return

class Simulate():
    def __init__(self, dt, objects, springs, methods):
        self.dt = dt
        self.objects = objects
        self.springs = springs
        for spring in self.springs:
            spring.rest_length = (((self.objects[spring.connect[0]].pos-self.objects[spring.connect[1]].pos)**2).sum())**0.5

        if 'mouse' in methods:
            self.app_mag = methods['mouse'][0]
            self.mouse_r = methods['mouse'][1]
            self.alpha = 0
            self.theta = 0
            self.mousepos = [0, 0, 0]

        if 'down grav' in methods:
            self.g = methods['down grav']

        if 'resist' in methods:
            self.drag_mag = methods['resist']

        if 'attract grav' in methods:
            self.G = methods['attract grav']

        self.methods = [method for method in methods]

        self.connections = []
        for spring in self.springs:
            if len(spring.connect) != 2:
               raise Exception(' {} Springs must be between TWO objects, try using a more objects, or throwing in some stationary objects'.format(len(spring.connect))) 

            self.connections.append([self.objects[spring.connect[0]], self.objects[spring.connect[1]]])

        if len(self.springs) > 0:
            self.methods.append('springs')

    def integrate(self):
        for obj in self.objects:
            a = obj.forces/obj.m
            obj.vel = obj.vel + a*self.dt
            obj.pos = obj.pos + obj.vel*self.dt
            obj.forces = np.array([0, 0, 0])
        return self.objects

    def forces(self):
        for obj in self.objects:
            if obj.dynamic == False:
                continue

            if 'down grav' in self.methods:
                force.weight(obj, self.g)
                
            if 'resist' in self.methods:
                force.drag(obj, self.drag_mag)
            
            if 'mouse' in self.methods:
                if ((self.mousepos[0]-obj.pos[0])**2 + (self.mousepos[1]-obj.pos[1])**2)**0.5 <= self.mouse_r:
                    force.push([self.app_mag*cos(self.alpha)*sin(self.theta), self.app_mag*-sin(self.alpha), self.app_mag*sin(self.theta)*cos(self.alpha)], obj)
        
        if 'springs' in self.methods:
            for spring in self.springs:
                force.spring(self.objects[spring.connect[0]], self.objects[spring.connect[1]], spring.rest_length, spring.k, spring.c) 

    def length_const(desired, obj1, obj2):
        length = np.linalg.norm(obj1-obj2)
        norm1 = (obj1-obj2)/length
        norm2 = (obj2-obj1)/length
        obj1.pos, obj2.pos = obj1.pos - desired/2 * norm1, obj2.pos - desired/2 * norm2
