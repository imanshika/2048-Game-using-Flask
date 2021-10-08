import random

def start_game():
    grid = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            grid[i][j] = 0
    add_new_2(grid)
    return grid


def add_new_2(grid):
    while(True):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        if (grid[r][c] == 0):
            grid[r][c] = 2
            break


def get_current_state(grid):
    for i in range(4):
        for j in range(4):
            if(grid[i][j] == 2048):
                return 1
    for i in range(4):
        for j in range(4):
            if((grid[i][j] == 0) or (i+1 < 4 and grid[i][j] == grid[i + 1][j]) or (j+1 < 4 and grid[i][j] == grid[i][j + 1])):
                return 0
    return -1


def compressLeft(grid):
    new_grid = [[0 for i in range(4)] for j in range(4)]
    change = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if(grid[i][j] != 0):
                new_grid[i][pos] = grid[i][j]
                if(j != pos):
                    change = True
                pos += 1
    return new_grid, change


def mergeLeft(grid):
    change = False
    for i in range(4):
        for j in range(3):
            if(grid[i][j] != 0 and grid[i][j] == grid[i][j+1]):
                grid[i][j] = 2*grid[i][j]
                grid[i][j+1] = 0
                change = True
    return grid, change


def reverse(grid):
    new_grid = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3 - j]
    return new_grid


def transpose(grid):
    new_grid = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    return new_grid


def isEmpty(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                return False
    return True

def move_left(grid):
    new_grid, change1 = compressLeft(grid)
    new_grid, change2 = mergeLeft(new_grid)
    new_grid, change3 = compressLeft(new_grid)
    return new_grid, change1 or change2 or change1

def move_right(grid):
    new_grid = reverse(grid)
    new_grid, change = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid, change


def move_up(grid):
    new_grid = transpose(grid)
    new_grid, change = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, change


def move_down(grid):
    new_grid = transpose(grid)
    new_grid, change = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, change
