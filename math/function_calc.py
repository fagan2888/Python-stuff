#Define reader for inputted equations
from math import *
def function(x, y,  equation):
    equation =  list(equation) 
    for i in range(len(equation)-1):
        if equation[i] == "x":
            equation[i] = str(x)
        if equation[i] == "y":
            equation[i] = str(y)
    equation = ''.join(equation)
    return eval(equation)
