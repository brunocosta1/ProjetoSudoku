# Arquivo responsável com as funções que vão resolver o sudoku.
import numpy

def is_possible(n, x, y):
    global grid
    for i in range(0,9):
        if grid[i][y] == n:
            return False

    for i in range(0, 9):
        if grid[x][i] == n:
            return False

    x1 = (x//3)*3
    y1 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x1+i][y1+j] == n:
                return False
    return True

def solve():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1,10):
                    if is_possible(n, x, y):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return
    print("Solução:\n")
    print(np.matrix(grid), "\n")
