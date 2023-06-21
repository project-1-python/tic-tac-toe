def board(grid):
    print('     |     |     ')
    for i in range(3):
        for j in range(3):
            print(f'  {grid[i][j]}  |', end='')

        print('\b')
        if i != 2:
            print('─────┼─────┼─────')
    print('     |     |     ')


def terminal(grid):
    filled = 0
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ' ':
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ' ':
            return True
        if ' ' not in grid[i]:
            filled += 1

    if filled == 3:
        return True

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != ' ':
        return True

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != ' ':
        return True

    return False


def actions(arr):
    actions_list = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == ' ':
                actions_list.append((i, j))

    return actions_list


def score(ch):
    if ch == 'X':
        return 1
    if ch == 'O':
        return -1


def value(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ' ':
            return score(grid[i][0])
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ' ':
            return score(grid[0][i])

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != ' ':
        return score(grid[1][1])

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != ' ':
        return score(grid[1][1])

    return 0


def player(ch):
    if ch == 'X':
        return 'MAX'
    return 'MIN'


def result(grid, r, ch):
    new_grid = grid.copy()
    new_grid[r[0]][r[1]] = ch
    return new_grid


def minimax(grid, ch='X'):
    if terminal(grid):
        return value(grid)
    if player(ch) == 'MAX':
        val = float("-inf")
        pass

    if player(ch) == "MIN":
        val = float("inf")
        pass


grid_1 = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
