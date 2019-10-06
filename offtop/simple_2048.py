from tkinter import *
from random import randint
import math
root = Tk()
root.title('2048')
color = ['#bbada0', '#eee4da', '#ede0c8', '#f2b179', '#f59563', '#f67c5f',
         '#f65e3b', '#edcf72', '#edcc61', '#edc850', '#edc53f', '#edc22e']
root['bg'] = color[0]
field = [[None] * 5 for i in range(5)]

for i in range(4):
    field[4][i] = Label(root, text=' ', height=1,
                        width=5, font='"Arial Black" 20', bg=color[0])
    field[4][i].grid(row=4, column=i)

for i in range(4):
    field[i][4] = Label(root, text=' ', height=3,
                        width=1, font='"Arial Black" 20', bg=color[0])
    field[i][4].grid(row=i, column=4)

field[4][4] = True


def game_over():

    for line in field:
        if None in line:
            return False
    for i in range(4):
        for j in range(3):
            if field[i][j]['text'] == field[i][j+1]['text']:
                return False
    for j in range(4):
            for i in range(3):
                if field[i][j]['text'] == field[i+1][j]['text']:
                    return False
    return True


def print_game_over():

    for i in range(4):

        field[4][i] = Label(root, text='END', height=1,
                            width=5, font='"Arial Black" 20', bg=color[0])
        field[4][i].grid(row=4, column=i)

    for i in range(4):

        field[i][4] = Label(root, text='END', height=3,
                            width=1, font='"Arial Black" 20', bg=color[0])
        field[i][4].grid(row=i, column=4)


def add_label():

    i, j = randint(0, 3), randint(0, 3)
    while field[i][j] is not None:
        i, j = randint(0, 3), randint(0, 3)
    field[i][j] = Label(root, text='2', font='"Arial Black" 20',
                        height=2, width=4, bg=color[1], fg='#776e65')
    field[i][j].grid(row=i, column=j)


def left(event):

    flag = False
    for i in range(4):
        free = 0
        for j in range(4):
            if field[i][j] is None:
                free += 1
            else:
                if free > 0:
                    field[i][j-free] = field[i][j]
                    field[i][j] = None
                    field[i][j-free].grid(row=i, column=j-free)
                    flag = True
                if j-free > 0:
                    if field[i][j-free]['text'] == field[i][j-free-1]['text']:
                        field[i][j-free].destroy()
                        field[i][j-free] = None
                        field[i][j-free-1]['text'] = str(int
                                                         (field[i][j-free-1]['text'])*2)
                        field[i][j-free-1]['bg'] = color[int(math.log2
                                                             (int(field[i][j-free-1]['text'])))]
                        free += 1
                        flag = True
    if flag:
        add_label()
        if game_over():
            print_game_over()


def right(event):

    flag = False
    for i in range(4):
        free = 0
        for j in range(3, -1, -1):
            if field[i][j] is None:
                free += 1
            else:
                if free > 0:
                    field[i][j+free] = field[i][j]
                    field[i][j] = None
                    field[i][j+free].grid(row=i, column=j+free)
                    flag = True
                if j + free < 3:
                    if field[i][j+free]['text'] == field[i][j+free+1]['text']:
                        field[i][j+free].destroy()
                        field[i][j+free] = None
                        field[i][j+free+1]['text'] = str(int
                                                         (field[i][j+free+1]['text'])*2)
                        field[i][j+free+1]['bg'] = color[int(math.log2
                                                             (int(field[i][j+free+1]['text'])))]
                        free += 1
                        flag = True
    if flag:
        add_label()
        if game_over():
            print_game_over()


def up(event):

    flag = False
    for j in range(4):
        free = 0
        for i in range(4):
            if field[i][j] is None:
                free += 1
            else:
                if free > 0:
                    field[i-free][j] = field[i][j]
                    field[i][j] = None
                    field[i-free][j].grid(row=i-free, column=j)
                    flag = True
                if i - free > 0:
                    if field[i-free][j]['text'] == field[i-free-1][j]['text']:
                        field[i-free][j].destroy()
                        field[i-free][j] = None
                        field[i-free-1][j]['text'] = str(int
                                                         (field[i-free-1][j]['text'])*2)
                        field[i-free-1][j]['bg'] = color[int(math.log2
                                                             (int(field[i-free-1][j]['text'])))]
                        free += 1
                        flag = True
    if flag:
        add_label()
        if game_over():
            print_game_over()


def down(event):

    flag = False
    for j in range(4):
        free = 0
        for i in range(3, -1, -1):
            if field[i][j] is None:
                free += 1
            else:
                if free > 0:
                    field[i+free][j] = field[i][j]
                    field[i][j] = None
                    field[i+free][j].grid(row=i+free, column=j)
                    flag = True
                if i + free < 3:
                    if field[i+free][j]['text'] == field[i+free+1][j]['text']:
                        field[i+free][j].destroy()
                        field[i+free][j] = None
                        field[i+free+1][j]['text'] = str(int
                                                         (field[i+free+1][j]['text'])*2)
                        field[i+free+1][j]['bg'] = color[int(math.log2
                                                             (int(field[i+free+1][j]['text'])))]
                        free += 1
                        flag = True
    if flag:
        add_label()
        if game_over():
            print_game_over()


if __name__ == "__main__":
    root.bind('<Left>', left)
    root.bind('<Right>', right)
    root.bind('<Up>', up)
    root.bind('<Down>', down)
    add_label()
    add_label()
    root.mainloop()
