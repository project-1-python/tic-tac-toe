import copy
import tkinter as tk
from tkinter import messagebox


def create_gui():
    global window, buttons

    window = tk.Tk()
    window.title("Tic Tac Toe")

    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(window, text=" ", width=10, height=5, command=lambda x=i, y=j: button_click(x, y))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)


def update_board(grid):
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = grid[i][j]


def button_click(x, y):
    global main_grid

    if main_grid[x][y] != ' ' or is_terminal(main_grid):
        return

    main_grid[x][y] = user
    buttons[x][y]["text"] = user

    if not is_terminal(main_grid):
        minimax(main_grid, computer)
        update_board(main_grid)

    if is_terminal(main_grid):
        if value(main_grid) == 1:
            messagebox.showinfo("Game Over", "Computer won the game!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")


def is_terminal(grid):
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

    if is_terminal(grid):
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
    create_gui()

    global main_grid

    window.mainloop()


main_grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

user = input("Enter your choice: (X or O): ").upper()
if user == 'X':
    user = '❌'
    computer = '⭕'
else:
    computer = '❌'

play_game()
