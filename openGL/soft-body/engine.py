from math import *
import numpy as np
import force
class Object():
    def __init__(self, m, pos, vel, dynamic=True, forces=[0,0,0]):
        self.dynamic = dynamic
        self.m = float(m)
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.forces = np.array(forces)
        return

class Spring():
    def __init__(self, k, c, connect):
        self.connect = connect
        self.k = k
        self.c = c
        return

class Engine():
    def __init__(self, dt, objects, springs):
        self.dt = dt
        self.objects = objects
        self.springs = springs
        for spring in self.springs:
            spring.rest_length = (((self.objects[spring.connect[0]].pos-self.objects[spring.connect[1]].pos)**2).sum())**0.5

    def integrate(self):
        points = []
        for obj in self.objects:
            a = obj.forces/obj.m
            obj.vel = obj.vel + a*self.dt
            obj.pos = obj.pos + obj.vel*self.dt
            obj.forces = np.array([0, 0, 0])
            points.append(obj.pos)

        return points
        

    def forces(self, g, G, drag_mag, app_mag):
        index = 0
        for obj in self.objects:
            if obj.dynamic == False:
                continue
            force.weight(obj, g)
            force.drag(obj, drag_mag)

#       MAKE SIMILTANEOUS
#        for obj2 in objects_old[:index]+objects_old[index+1:]:
#            obj.forces = obj.forces + force.grav(obj, obj2, 7.5)

            index += 1
        return

    def spring_sim(self):
        connections = []
        for spring in self.springs:
            if len(spring.connect) == 1:
               raise Exception(' {} Springs must be between atleast TWO objects, try using a stationary object instead'.format(len(spring.connect))) 

            connections.append([self.objects[spring.connect[0]], self.objects[spring.connect[1]]])

            force.spring(self.objects[spring.connect[0]], self.objects[spring.connect[1]], spring.rest_length, spring.k, spring.c)

        return connections

    def mouse_interact(self, mousepos, alpha, theta, r, app_mag):
        for obj in self.objects:
            if obj.dynamic == False:
                continue
            if ((mousepos[0]-obj.pos[0])**2 + (mousepos[1]-obj.pos[1])**2)**0.5 <= 3*r:
                force.push([app_mag*cos(alpha)*sin(theta), app_mag*-sin(alpha), app_mag*sin(theta)*cos(alpha)], obj)





def length_const(desired, obj1, obj2):
    length = (((obj2.pos-obj1.pos)**2).sum())**0.5
    norm1, norm2 = (obj2.pos-obj1.pos)/length, (obj1.pos-obj2.pos)/length
    obj1.pos, obj2.pos = obj1.pos + norm1*desired/2, obj2.pos + norm2*desired/2 
    return

