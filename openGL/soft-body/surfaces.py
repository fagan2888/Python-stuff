from math import * 
def cloth(n, dis, inc=pi/2, pos=[0, 0, 0], points=[], cur=0):
    if cur > n:
        return

    theta = 0
    while theta < 2*pi:
        new = [cos(theta)*dis+pos[0], sin(theta)*dis+pos[1], 0]
        if [round(z) for z in new] not in [[round(k) for k in p] for p in points]:
            points.append(new)
            cloth(n, dis, inc, new, points, cur+1)
        theta += inc
    return points
