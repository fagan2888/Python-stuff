#Every time that a y value is changed: call a function that checks if any x values are below it and, if so, sends them through all possible ys. Method to change the current position of a number
import numpy as np
my_list = [i for i in range(1, 9)]
print(my_list)
board = np.zeros((7,8))
print(board)
board = np.insert(board, 0, np.ones(8), axis = 0) 
print(board)
#for y in range(8):
#    for x in range(8):

