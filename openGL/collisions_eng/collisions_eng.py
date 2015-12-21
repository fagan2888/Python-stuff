import numpy as np
import copy, math, decimal
from decimal import Decimal as D
import multiprocessing as mp

def ring(r, v, inc):

   theta = 0
   planets = []

   while theta < 2*math.pi:

      planets.append(ObjectDetailed(1, [r*math.cos(theta), r*math.sin(theta), 0], [v*math.cos(theta+math.pi/2), v*math.sin(theta+math.pi/2), 0], 1))
      theta += inc
    
   return planets


class ObjectDetailed:
    def __init__(self, m, s, v, r):
        self.m = D(m)
        self.r = r
        self.v = np.array([D(i) for i in v])
        self.s = np.array([D(i) for i in s])
        self.a_prev = ''

class UniverseDetailed:
    def __init__(self, G, dt, methods, bounds, t):
        self.G = D(G)
        self.dt = D(dt)
        self.t = t
        self.methods = methods
        self.bounds = [D(b) for b in bounds]


    def time_step(self, objects):

        index = 0
        objects_old = [Object(p.m, p.s, p.v, p.r) for p in objects]

        for p in objects:
            p.a = np.array([D(0) for i in range(3)])

            for pdif in objects_old[:index]+objects_old[index+1:]: 
                r = D(math.sqrt(((pdif.s-p.s)**2).sum()))
                
                if 'grav' in self.methods:
                    self.attract(p, pdif, r)

                if 'coll' in self.methods:
                    self.collision(p, pdif, r)
                    
            if 'cube' in self.methods:
                p.v += p.a*self.dt
                self.in_cube(p)
                p.s += p.v*self.dt

            else:
                p.v += p.a*self.dt
                p.s += p.v*self.dt
             
            index += 1

        self.t += self.dt

        return objects

    def attract(self, p, pdif, r):
        p.a += (pdif.s-p.s)*self.G*pdif.m*r**(-3)


    def collision(self, p, pdif, r):
        if r <= p.r+pdif.r:
            p.v = (p.v * (p.m-pdif.m) + 2 * pdif.m * pdif.v)/(p.m + pdif.m)

    def in_cube(self, p):
        for c in range(len(p.s)):
            if p.s[c]+p.r >= self.bounds[c] and p.v[c] > 0:
                p.v[c] *= -1
            if p.s[c]+p.r <= -self.bounds[c] and p.v[c] < 0:
                p.v[c] *= -1
class Object:
    def __init__(self, m, s, v, r):
        self.m = m
        self.r = r
        self.v = np.array([float(i) for i in v])
        self.s = np.array([float(i) for i in s])

class Universe:
    def __init__(self, G, dt, methods, bounds, t):
        self.G = float(G)
        self.dt = float(dt)
        self.t = t
        self.methods = methods
        self.bounds = bounds


    def time_step(self, objects):

        index = 0
        objects_old = [Object(p.m, p.s, p.v, p.r) for p in objects]

        for p in objects:
            p.a = np.array([0, 0, 0])

            for pdif in objects_old[:index]+objects_old[index+1:]: 
                r = (((pdif.s-p.s)**2).sum())**0.5
                
                if 'grav' in self.methods:
                    self.attract(p, pdif, r)

                if 'coll' in self.methods:
                    self.collision(p, pdif, r)
                    
            if 'cube' in self.methods:
                p.v = p.v + p.a*self.dt
                self.in_cube(p)
                p.s = p.s + p.v*self.dt

            else:
                p.v = p.v + p.a*self.dt
                p.s = p.s + p.v*self.dt
             
            index += 1

        self.t += self.dt

        return objects

    def attract(self, p, pdif, r):
        p.a = p.a + (pdif.s-p.s)*self.G*pdif.m*r**(-3)
        print(p.a)


    def collision(self, p, pdif, r):
        if r <= p.r+pdif.r:
            p.v = (p.v * (p.m-pdif.m) + 2 * pdif.m * pdif.v)/(p.m + pdif.m)

    def in_cube(self, p):
        for c in range(len(p.s)):
            if p.s[c]+p.r >= self.bounds[c] and p.v[c] > 0:
                p.v[c] *= -1
            if p.s[c]+p.r <= -self.bounds[c] and p.v[c] < 0:
                p.v[c] *= -1
