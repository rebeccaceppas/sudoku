import solver
import random

def starting(dimension=9):
    ''' Creates empty grid of given dimension '''
    grid = [[0 for i in range(dimension)] for i in range(dimension)]
    return grid

def fill_board():
    grid = starting()
    puzzle = solver.solve(grid)
    return puzzle


