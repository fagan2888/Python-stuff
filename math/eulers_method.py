import matplotlib.pyplot as plt
from sys import argv
from math import e
from math import sin
from math import cos
from math import log
from math import sqrt 
from function_calc import function as fc

class Approximate:
#Constructor method:
    def __init__(self, steps, initial_x, initial_y, final_x, equation):
        self.steps = float(steps)
        self.initial = float(initial_x)
        self.x = float(initial_x)
        self.y = float(initial_y)
        self.limit = float(final_x)
        self.equation = equation
        self.xs = []
        self.ys = []
    
#Running method that evaluates different values and prints table of method answers
    def run(self):
        while self.x < self.limit:
            self.xs.append(self.x)
            self.ys.append(self.y)
            dydx = float(fc(self.x, self.y, self.equation))
            Dx = (self.limit-self.initial)/self.steps
            Dy = float(Dx*dydx)
            self.y = float(self.y + Dy)
            self.x = float(100*(self.x + Dx))/100
            print("x: ", self.x, "| y: ",  self.y,  "| dy/dx: ", dydx, "| Dx: ", Dx, "| Dy: ", Dy)
        
#eulers = Approximate(argv[1], argv[2], argv[3], argv[4], argv[5])
#import pdb; pdb.set_trace()
euler = Approximate(2, -1, 2, 0, '6*(x**2)-y*(x**2)')
euler.run()
plt.plot(euler.xs, euler.ys)
plt.show()
