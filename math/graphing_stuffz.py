import numpy as np
import matplotlib.pyplot as plt
def equation(x, y):
    return x**2 + y**2

variables = np.arange(-1, 1, 0.001)

plt.plot(np.exp(variables)) 
plt.show()
