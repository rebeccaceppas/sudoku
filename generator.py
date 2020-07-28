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
    value = board[position[0]][position[1]]
    board[position[0]][position[1]] = 0
    print(board)
    return board, value

def main():
    ''' Returns final puzzle to player '''
    puzzle = fill_board()
    givens = 81
    done = False
    while (not done) and givens >= 17:
        pos = cell(puzzle)
        puzzle, value = remove(pos, puzzle)
        if solver.solve(puzzle) == False:
            puzzle[pos[0]][pos[1]] = value
            givens += 1
        givens -= 1

    print(puzzle)
    return puzzle

main()