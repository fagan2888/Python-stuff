from sys import argv
import numpy as np
import string
def board_maker(blank, black, white):
    rows = [blank + string.ascii_uppercase[:8]]
    first_row = []
    second_row = []
    for i in range(32):
        if i == 0:
            first_row.append(i % 4 + 1)
##############################            first_row.append(blank)
#            first_row.append(black)
        elif i <= 4:
            first_row.append(blank)
            first_row.append(black)
        elif i == 5:
            second_row.append(i % 4 + 1)
            second_row.append(black)
            second_row.append(blank)
        elif i <= 8:
            second_row.append(black)
            second_row.append(blank)
    board = np.matrix([rows, first_row, second_row])
    print(board)

board_maker("||", "o", 2)
#class Checkers:
#    def __init__(self):
#        if argv[1] == "default":
#            self.board = np.matrix([[" ", "a", "b", "c", "d", "e", "f", "g", "h"], [, 1, 2, 3, 4, 5, 6, 7, 8]])
#            print(self.board)
#Checkers()
