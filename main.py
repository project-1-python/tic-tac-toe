import copy


def board(grid=None):
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


def value(grid=None):
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
    new_grid = copy.deepcopy(grid)
    new_grid[r[0]][r[1]] = ch
    return new_grid.copy()


def minimax(mgrid, ch='X', t=0):
    global main_grid
    grid = mgrid.copy()
    if terminal(grid):
        return value(grid)
    if player(ch) == 'MAX':
        old = -98
        val = -98
        i, j = None, None
        for positions in actions(grid):
            val = max(val, minimax(result(grid, positions, 'X'), 'O', 1))
            if old < val:
                i, j = positions
                old = val

        if t == 0:
            main_grid[i][j] = 'X'
        return val

    if player(ch) == "MIN":
        val = 99
        for positions in actions(grid):
            val = min(val, minimax(result(grid, positions, 'O'), 'X', 1))

        return val


def play_game():
    global main_grid

    while not terminal(main_grid):
        while True:
            pos = int(input("Enter position: ")) - 1
            if (pos // 3, pos % 3) in actions(main_grid):
                main_grid[pos // 3][pos % 3] = 'O'
                break
            else:
                print('enter valid number.')

        minimax(main_grid, 'X')
        board(main_grid)
    else:
        if value(main_grid) == 1:
            print('Computer Won the Game.')
        else:
            print('Draw.')


main_grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

play_game()
