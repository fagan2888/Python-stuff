from graphics import *
import math
win = GraphWin('Face', 1000, 500) # give title and dimensions

Ans = [100]
Bns = [-50]
Sns = [0]
points = [Point(450, 300)]
lines = []

rect = Rectangle(points[0], Point(550, 250))
rect.setFill("red")
rect.draw(win)


def run():
    for x in range(5):
        Ans.append(math.sqrt(Ans[x]**2 + Bns[x]*2))
        Sns.append(Bns[x]**2/Ans[x+1])
        Bns.append(-math.sqrt(Bns[x]**2-Sns[x+1]**2))
        points.append(Point(Ans[x]+450, Bns[x]+300))
        points.append(Point(Ans[x+1]+450, Bns[x+1]+300))
        lines.append(Line(points[0], points[1]))
        lines.append(Line(points[1], points[2]))
        lines[0].draw(win)
        lines[1].draw(win)
#        Line3 = Line(Point(An, Bn), Point(450-Sn, 
        win.getMouse()
        win.close()
        print(Ans)

run()
