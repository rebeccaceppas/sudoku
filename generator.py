import solver
import random


def random_grid():
    ''' Creates grid with random numbers 1-9 '''
    grid = [[random.randint(1,9) for i in range(9)] for j in range(9)]
    return grid

def check_valid(grid):
    ''' Checks if all numebrs of the grid are valid '''
    # check rows
    for i in range(len(grid)):
        if len(set(grid[i])) != len(grid[i]):
            return False

    # check columns
    cols = list(zip(*grid))  
    for i in range(len(cols)):
        if len(cols[i]) != len(set(cols[i])):
            return False

    # check boxes
    box = []
    box_row = 0
    box_column = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):         
            box_row = i // 3
            box_column = j // 3  
            for i in range(box_row * 3, box_row * 3 + 3):
                for j in range(box_column * 3, box_column * 3 + 3):
                    box.append(grid[i][j])            
            if len(box) != len(set(box)):
                return False

    # If none of them fail, we have succeeded 
    return True

def main():
    success = False
    while not success:
        grid = random_grid()
        if check_valid(grid):
            return grid

main()