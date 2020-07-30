import random

grid2 = [
    [0, 0, 0, 5, 7, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 3, 0, 4, 0],
    [7, 5, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 2, 0, 0, 4, 0, 7, 0],
    [1, 8, 0, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 2, 0, 0, 9, 0, 0, 1, 3],
    [6, 4, 0, 3, 0, 8, 0, 5, 7],
    [5, 0, 1, 0, 0, 6, 0, 0, 0]
]

grid = [
    [0, 0, 1, 4, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 7, 8, 0, 4, 0],
    [4, 5, 0, 0, 0, 2, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 5, 1, 0],
    [0, 6, 0, 0, 0, 0, 0, 2, 0],
    [0, 2, 7, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 2, 0, 0, 0, 5, 6],
    [0, 7, 0, 6, 9, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 4, 1, 0, 0]
]

def print_board(board):
    ''' Prints out current grid '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-------------------')

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end='')

            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + ' ', end='')


def empty(board):
    ''' Returns coordinates of empty square (row, column) '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return False  # the grid is complete


def valid(board, position, number):
    ''' Checks if it is valid to input a number into chosen position of current grid '''
    for i in range(len(board)):
        if board[position[0]][i] == number and board[position[1]] != i:
            return False

    for i in range(len(board[0])):
        if board[i][position[1]] == number and board[position[0]] != i:
            return False

    box_column = position[1] // 3
    box_row = position[0] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_column * 3, box_column * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    
    return True

def solve(board):
    ''' Returns solved puzzle, using backtracking '''
    if not empty(board):
        return board
    else:
        row, column = empty(board)
    l = list(range(1,10))
    random.shuffle(l)
    for i in l:
        if valid(board, (row, column), i):
            board[row][column] = i

            if solve(board):
                return board

            board[row][column] = 0

    return False