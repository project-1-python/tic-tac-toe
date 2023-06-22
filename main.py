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
    if ch == computer:
        return 1
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


def result(grid, pos, ch):
    new_grid = copy.deepcopy(grid)
    new_grid[pos[0]][pos[1]] = ch
    return new_grid.copy()


def minimax(grid, choice, t=0):
    global main_grid

    if terminal(grid):
        return value(grid)

    if computer == choice:  # MAX
        old, val = -98, -98
        i, j = None, None
        for positions in actions(grid):
            val = max(val, minimax(result(grid, positions, computer), user, 1))
            if old < val:
                i, j = positions
                old = val

        if t == 0:
            main_grid[i][j] = computer
        return val

    if user == choice:  # MIN
        val = 99
        for positions in actions(grid):
            val = min(val, minimax(result(grid, positions, user), computer, 1))

        return val


def play_game():
    global main_grid

    while not terminal(main_grid):
        while True:
            pos = int(input("Enter position: ")) - 1
            if (pos // 3, pos % 3) in actions(main_grid):
                main_grid[pos // 3][pos % 3] = user
                break
            else:
                print('enter valid number.')

        minimax(main_grid, computer)
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

user = input("Enter your choice: (X or O): ").upper()
if user == 'X':
    computer = 'O'
else:
    computer = 'X'

play_game()
