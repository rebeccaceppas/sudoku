import solver
import random

#counter = 0

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

def generate():
    ''' Returns final puzzle to player '''
    puzzle = fill_board()
    complete = [ x[:] for x in puzzle ]
    givens = 81
    while givens > 28:
        pos = cell(puzzle)
        puzzle = remove(pos, puzzle)
        givens -= 1
    print(puzzle)
    print(complete)
    return puzzle, complete


def main():
    saved_puzzle = list()
    puzzle, complete = generate()
    saved_puzzle = complete = [ x[:] for x in puzzle ]
    print('\n this is saved puzzle\n ')
    print(saved_puzzle)
    print('\n this is complete puzzle\n')
    print(complete)
    result = solver.solve(puzzle)
    attempt = 0
    while complete != result:
        puzzle, complete = generate()
        saved_puzzle = complete = [ x[:] for x in puzzle ]
        solver.print_board(puzzle)
        result = solver.solve(puzzle)
        attempt += 1
        print(attempt)

    print('\n This is the solved puzzle: \n')
    solver.print_board(saved_puzzle)
    print()
    
    return saved_puzzle


main()
