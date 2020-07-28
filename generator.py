import solver
import random

def starting(dimension=9):
    ''' Returns empty grid of given dimension '''
    grid = [[0 for i in range(dimension)] for i in range(dimension)]
    return grid

def fill_board():
    ''' Returns filled board with numbers for valid puzzle '''
    grid = starting()
    puzzle = solver.solve(grid)
    return puzzle

def cell(board):
    ''' Returns coordinates of random non-empty cell '''
    l1 = list(range(len(board)))
    random.shuffle(l1)
    for i in l1:
        l2 = list(range(len(board[i])))
        random.shuffle(l2)
        for j in l2:
            if board[i][j] != 0:
                return (i, j)

def remove(position, board):
    ''' Removes current number on given position of grid '''
    board[position[0]][position[1]] = 0
    return board


def main():
    ''' Returns final puzzle to player '''
    puzzle = fill_board()
    print(puzzle)
    givens = 81
    while givens > 28:
        pos = cell(puzzle)
        puzzle = remove(pos, puzzle)
        givens -= 1

    print(givens)

    return puzzle

puzzle = main()
solver.print_board(puzzle)
solver.solve(puzzle)
print()
solver.print_board(puzzle)