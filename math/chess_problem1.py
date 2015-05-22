import numpy as np
board = np.zeros((8,8))
for x in range(9):
    for y in range(9):
        board[x][y] = 1
        if x-2 % 2 == 0:
            zx = x + 1 
        else:
            zx = x - 1
        if y-2 % 2 == 0:
            zy = y + 1
        else:
            zy = y - 1
        board[zx][zy] = 1
        board[x][zy] = 1
        board[zx][y] = 1
        print(board, "\n", zx, zy, x, y)
        board = np.zeros((8,8))
