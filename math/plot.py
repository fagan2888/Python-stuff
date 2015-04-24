import numpy as np  
import matplotlib.pyplot as plt  
from math import e
def graph(formula, x_range):  
        x = np.array(x_range)  
        y = eval(formula)
        plt.plot(x, y)  
        plt.show()
graph('e**x', range(-10, 11))
