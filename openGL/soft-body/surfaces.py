from engine import *
def cloth(lim, struc_k, shear_k, bend_k, c, m, dis, mode='square'):
    springs = []
    objects = []

    for row in range(-lim, lim+1):
        points = []

        for x in range(-lim, lim+1):
            point = [dis*x, 0, dis*row]
            points.append(point)

        for point in points:
            if mode == 'square':
                if point == points[0] or point == points[-1] or abs(row) == lim:
                    objects.append(Object(m, point, [0, 0, 0], 1, False))
                else:
                    objects.append(Object(m, point, [0, 0, 0], 1))
            if mode == '4 edges':
                if point == points[0] and abs(row) == lim or point == points[-1] and abs(row) == lim:
                    objects.append(Object(m, point, [0, 0, 0], 1, False))
                else:
                    objects.append(Object(m, point, [0, 0, 0], 0.5))
            if mode == '1 edge':
                if point == points[0] and row == lim:
                    objects.append(Object(m, point, [0, 0, 0], 1, False))
                else:
                    objects.append(Object(m, point, [0, 0, 0], 0.5))

    for x in range(len(points)):
        for y in range(len(points)):
            if x < len(points)-1:
                springs.append(Spring(struc_k, c, [x+y*len(points), x+y*len(points)+1]))
            if x < len(points)-2:
                springs.append(Spring(struc_k, c, [x+y*len(points), x+y*len(points)+2]))
            if y < len(points)-1:
                springs.append(Spring(bend_k, c, [x+y*len(points), x+(y+1)*len(points)]))
            if y < len(points)-2:
                springs.append(Spring(bend_k, c, [x+y*len(points), x+(y+2)*len(points)]))
            
            if len(points)-1 > x > 0 and len(points)-1 > y > 0:
                springs.append(Spring(shear_k, c, [x+y*len(points), x+1+(y+1)*len(points)]))
                springs.append(Spring(shear_k, c, [x+y*len(points), x+1+(y-1)*len(points)]))
                springs.append(Spring(shear_k, c, [x+y*len(points), x-1+(y+1)*len(points)]))
                springs.append(Spring(shear_k, c, [x+y*len(points), x-1+(y-1)*len(points)]))

    return springs, objects
