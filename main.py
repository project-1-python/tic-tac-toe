def board(grid):
    print('     |     |     ')
    for i in range(3):
        for j in range(3):
            print(f'  {grid[i][j]}  |', end = '')

        print('\b')
        if i != 2:
            print('─────┼─────┼─────')
    print('     |     |     ')


def terminal_state(grid, ch = 'X'):
    d1, d2 = 0, 0
    filled = 0

    # rows, cols and draw check
    for i in range(3):
        r, c = 0, 0
        for j in range(3):
            if grid[i][j] == ch:
                r += 1
            if grid[j][i] == ch:
                c += 1
            if grid[i][j] != ' ':
                filled += 1
        if r == 3 or c == 3 or filled == 9:
            return True

    # diagonal check
    for i in range(3):
        if grid[i][i] == ch:
            d1 += 1
        if grid[i][2 - i] == ch:
            d2 += 1

    if d1 == 3 or d2 == 3:
        print("diag")
        return True

    if ch == 'X':
        return terminal_state(grid, 'O')

    return False

def value(s):
    n = 0
    d1, d2 = 0, 0
    c = ['X', 'O']
    while n < 2:
        ch = c[n]
        for i in range(3):
            r, c = 0, 0
            for j in range(3):
                if s[i][j] == ch:
                    r += 1
                if s[j][i] == ch:
                    c += 1
            if r == 3 or c == 3:
                if ch == 'X':
                    return 1
                return -1

        # diagonal check
        for i in range(3):
            if s[i][i] == ch:
                d1 += 1
            if s[i][2 - i] == ch:
                d2 += 1

        if d1 == 3 or d2 == 3:
            if ch == 'X':
                return 1
            return -1
        n += 1

        return 0


def actions(arr):
    actions_list = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                actions_list.append((i, j))

    return actions_list


def player(ch):
    if ch == 'X':
        return 1
    return 2


def minimax(s):
    if terminal_state(s):
        return value(s)


grid_1 = [
    ['O', ' ', 'X'],
    ['O', 'O', 'X'],
    ['O', 'X', 'O']
]

print(terminal_state(grid_1))
print(value(grid_1))
