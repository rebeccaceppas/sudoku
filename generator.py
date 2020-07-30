import solver
import random

counter = 0

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

""" def solutions(board):
    ''' Counts number of solutions for puzzle '''
    global counter
    if not solver.empty(board):
        counter += 1
    else:
        pos = solver.empty(board)
    l = list(range(1,10))
    random.shuffle(l)
    for i in l:
        if solver.valid(board, pos, i):
            board[pos[0]][pos[1]] = i

            if solutions(board):
                return True

            board[pos[0]][pos[1]] = 0

    return False """

def solutions(board, position):
    ''' Counts number of solutions for puzzle '''
    global counter
    if not solver.empty(board):
        counter += 1
        return
    l = list(range(1,10))
    random.shuffle(l)
    for i in l:
        if solver.valid(board, position, i):
            board[position[0]][position[1]] = i

            if solutions(board, position):
                return True

            board[position[0]][position[1]] = 0

    return False

""" def main():
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
solver.print_board(puzzle) """

def main():

    puzzle = fill_board()
    attempts = 5

    while attempts > 0:
        pos = cell(puzzle)
        value = puzzle[pos[0]][pos[1]]
        puzzle = remove(pos, puzzle)
        print('\nThis is the puzzle at this stage: \n', puzzle)

        copy_puzzle = []
        for r in range(0, 9):
            copy_puzzle.append([])
            for c in range(0, 9):
                copy_puzzle[r].append(puzzle[r][c])

        solutions(copy_puzzle, pos)
        print('\nThe counter is: ', counter)
        if counter != 1:
            puzzle[pos[0]][pos[1]] = value
            attempts -= 1

    return puzzle


main()
""" solver.print_board(puzzle)
solver.solve(puzzle)
print()
solver.print_board(puzzle) """

