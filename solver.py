grid = [
    [' ', ' ', ' ', 5, 7, ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 9, ' ', 3, ' ', 4, ' '],
    [7, 5, ' ', ' ', ' ', 2, ' ', ' ', ' '],
    [' ', ' ', 2, ' ', ' ', 4, ' ', 7, ' '],
    [1, 8, ' ', ' ', ' ', ' ', 4, 2, ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 1],
    [8, 2, ' ', ' ', 9, ' ', ' ', 1, 3],
    [6, 4, ' ', 3, ' ', 8, ' ', 5, 7],
    [5, ' ', 1, ' ', ' ', 6, ' ', ' ', ' ']
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
            if board[i][j] == ' ':
                return (i, j)
    return None

def valid(board, position, number):
    ''' Checks if it is valid to input a number into chosen position of current grid '''
    square = empty(board)
    
    for i in range(len(board)):
        if board[square[0]][i] == number and board[square[1]] != i:
            return False

    for i in range(len(board[0])):
        if board[i][square[1]] == number and board[square[0]] != i:
            return False

    box_column = square[1] // 3
    box_row = square[0] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_column * 3, box_column * 3 + 3):
            if board[i][j] == number and (i,j) != square:
                return False
    
    return True

def solve(board):
    ''' Uses backtracking to solve the sudoku puzzle '''

    if not empty(board):
        return True
    else:
        row, column = empty(board)

    for i in range(1,10):
        if valid(board, (row, column), i):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = ' '

    return False



print_board(grid)
solve(grid)
print('')
print_board(grid)