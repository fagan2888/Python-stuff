import math 
def cube(s, dim):
    x = s[0]
    y = s[1]
    z = s[2]
    l = dim[0]
    h = dim[1]
    w = dim[2]

    points = []
    lines = []
    for i in [l/2, -l/2]:
        for j in [-h/2, h/2]:
            for k in [-w/2, w/2]:
                points.append([x+i, y+j, z+k])

    edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]

    for edge in edges:
        lines.append((points[edge[0]], points[edge[1]]))

    return lines
