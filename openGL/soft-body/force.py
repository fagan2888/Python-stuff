import numpy as np
def weight(obj, g):
    obj.forces = obj.forces - np.array([0, obj.m*g, 0])

def grav(obj1, obj2, G):
  dis1 = obj2.pos-obj1.pos
  dis2 = -dis1
  r = ((dis1**2).sum())**0.5

  obj1.forces, obj2.forces = obj1.forces + dis1*G*obj1.m*obj2.m*r**(-3), obj2.forces + dis2*G*obj1.m*obj2.m*r**(-3)

def push(mags, obj):
  obj.forces = obj.forces + np.array(mags)

def drag(obj, drag_force):
  obj.forces = obj.forces - obj.vel * drag_force

def spring(obj1, obj2, rest_length, k, c):
    cur_length = (((obj1.pos-obj2.pos)**2).sum())**0.5
    norm1 = (obj1.pos-obj2.pos)/(((obj2.pos-obj1.pos)**2).sum())**0.5
    norm2 = (obj2.pos-obj1.pos)/(((obj1.pos-obj2.pos)**2).sum())**0.5

    if obj2.dynamic == False:
        obj1.forces = obj1.forces - k * (cur_length-rest_length) * norm1 - c * ((obj1.vel-obj2.vel)*norm1).sum() * norm1

    elif obj1.dynamic == False:
        obj2.forces = obj2.forces - k * (cur_length-rest_length) * norm2 - c * ((obj2.vel-obj1.vel)*norm2).sum() * norm2

    else:
        obj1.forces, obj2.forces = obj1.forces - k * (cur_length-rest_length) * norm1 - c * ((obj1.vel-obj2.vel)*norm1).sum() * norm1, obj2.forces - k * (cur_length-rest_length) * norm2 - c * ((obj2.vel-obj1.vel)*norm2).sum() * norm2


def oppose(obj):
  obj.forces = -obj.forces
