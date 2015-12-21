import numpy as np
def weight(obj, g):
    obj.forces = obj.forces - np.array([0, obj.m*g, 0])

def grav(obj1, obj2, G):
  dis1 = obj2.pos-obj1.pos
  r = ((dis1**2).sum())**0.5

  obj1.forces = obj1.forces + dis1*G*obj1.m*obj2.m*r**(-3)

def push(mags, obj):
  obj.forces = obj.forces + np.array(mags)

def drag(obj, drag_force):
  obj.forces = obj.forces - obj.vel * drag_force

def spring(obj1, obj2, rest_length, k, c):
    cur_length = np.linalg.norm(obj1.pos-obj2.pos)
    norm1 = (obj1.pos-obj2.pos)/(cur_length)
    norm2 = (obj2.pos-obj1.pos)/(cur_length)

    if not obj2.dynamic:
        obj1.forces = obj1.forces - k * (cur_length-rest_length) * norm1 - c* np.dot(obj1.vel-obj2.vel, norm1) * norm1

    elif not obj1.dynamic:
        obj2.forces = obj2.forces - k * (cur_length-rest_length) * norm2 - c* np.dot(obj2.vel-obj1.vel, norm2) * norm2

    else:
        obj1.forces, obj2.forces = obj1.forces - k * (cur_length-rest_length) * norm1 - c * np.dot(obj1.vel-obj2.vel, norm1) * norm1,  obj2.forces - k * (cur_length-rest_length) * norm2 - c * np.dot(obj2.vel-obj1.vel, norm2) * norm2

def oppose(obj):
  obj.forces = -obj.forces
