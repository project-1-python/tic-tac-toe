import copy
from tkinter import *
from tkinter import messagebox


def create_gui():
    global window, buttons

    window = Tk()
    window.title("Tic Tac Toe")
    Label(window, text = "TIC TAC TOE", font = ('consolas', 35)).grid(row=0, column=0, columnspan=35)
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = Button(window, text=" ", width=3, height=1, font=('consolas', 40),
                            command=lambda x=i, y=j: button_click(x, y), bg='#FBEAEB', fg='red')
            button.grid(row=i+1, column=j)
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
            grid = main_grid
            for i in range(3):
                if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != ' ':
                    buttons[i][0].config(bg='#00FFFF')
                    buttons[i][1].config(bg='#00FFFF')
                    buttons[i][2].config(bg='#00FFFF')
                if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != ' ':
                    buttons[0][i].config(bg='#00FFFF')
                    buttons[1][i].config(bg='#00FFFF')
                    buttons[2][i].config(bg='#00FFFF')

            if grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] != ' ':
                buttons[0][0].config(bg='#00FFFF')
                buttons[1][1].config(bg='#00FFFF')
                buttons[2][2].config(bg='#00FFFF')

            if grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] != ' ':
                buttons[0][2].config(bg='#00FFFF')
                buttons[1][1].config(bg='#00FFFF')
                buttons[2][0].config(bg='#00FFFF')
            messagebox.showinfo("Game Over", "Computer won the game!")

            window.destroy()
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
            window.destroy()


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


def fun_1():
    global user, computer
    user, computer = "❌", "⭕"
    root.destroy()
    play_game()


def fun_2():
    global user, computer
    user, computer = "⭕", "❌"
    root.destroy()
    play_game()


def play_game():
    create_gui()

    global main_grid

    window.mainloop()


main_grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

root = Tk()
root.title("TIC TAC TOE")

Label(root, text="Enter your choice (X or O): ", font='consolas').grid(row=0, column=0, columnspan=3)
Button(root, text="❌", command=fun_1, width=8, height=5, bg='red', padx=47, pady=10, font='consolas').grid(row=1, column=0)
Button(root, text="⭕", command=fun_2, width=8, height=5, bg='green', padx=47, pady=10, font='consolas').grid(row=1, column=1)

root.mainloop()
