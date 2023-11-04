import numpy as np

sudoku_grid = [
    [0, 0, 0, 8, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 3],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 0, 3, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 7, 5],
    [0, 0, 3, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 6, 0, 0],
]


def check_num(y, x, n):
    global sudoku_grid
    for i in range(0, 9):
        if sudoku_grid[y][i] == n:
            return False
    for i in range(0, 9):
        if sudoku_grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_grid[y0 + i][x0 + j] == n:
                return False
    return True


def solution():
    global sudoku_grid
    for y in range(0, 9):
        for x in range(0, 9):
            if sudoku_grid[y][x] == 0:
                for n in range(1, 10):
                    if check_num(y, x, n):
                        sudoku_grid[y][x] = n
                        solution()
                        sudoku_grid[y][x] = 0
                return
    print(np.matrix(sudoku_grid))
    input("devam?")


solution()
