from tkinter import *
from math import *

SIZE_X = 600
SIZE_Y = 500
STEP = 8


class Curve:
    def __init__(self, canvas):
        self.canvas = canvas

    def pen(self, yes):
        self.pen = yes

    def move(self, x_move, y_move):
        self.x = x_move
        self.y = y_move

    def make_curve(self, angle, length):
        upd_x = self.x + cos(pi / 180 * angle) * length
        upd_y = self.y + sin(pi / 180 * angle) * length
        cx = SIZE_X / 2
        cy = SIZE_Y / 2
        if self.pen:
            self.canvas.create_line(cx + self.x, cy - self.y, cx + upd_x, cy - upd_y, fill=COLOR[0])
        self.x = upd_x
        self.y = upd_y


class Serpin:

    def __init__(self, curve):
        self.curve = curve

    def doit(self, level):
        self.curve.move(-1.6 * STEP * pow(2, level) - 1, -1.6 * STEP * pow(2, level) - 1)
        self.A(level)
        self.curve.make_curve(-315, STEP)
        self.B(level)
        self.curve.make_curve(-225, STEP)
        self.C(level)
        self.curve.make_curve(-135, STEP)
        self.D(level)
        self.curve.make_curve(-45, STEP)

    def A(self, i):
        if i > 0:
            self.A(i - 1)
            self.curve.make_curve(45, STEP)
            self.B(i - 1)
            self.curve.make_curve(0, 2 * STEP)
            self.D(i - 1)
            self.curve.make_curve(-45, STEP)
            self.A(i - 1)

    def B(self, i):
        if i > 0:
            self.B(i - 1)
            self.curve.make_curve(135, STEP)
            self.C(i - 1)
            self.curve.make_curve(90, 2 * STEP)
            self.A(i - 1)
            self.curve.make_curve(45, STEP)
            self.B(i - 1)

    def C(self, i):
        if i > 0:
            self.C(i - 1)
            self.curve.make_curve(-135, STEP)
            self.D(i - 1)
            self.curve.make_curve(180, 2 * STEP)
            self.B(i - 1)
            self.curve.make_curve(135, STEP)
            self.C(i - 1)

    def D(self, i):
        if i > 0:
            self.D(i - 1)
            self.curve.make_curve(-45, STEP)
            self.A(i - 1)
            self.curve.make_curve(-90, 2 * STEP)
            self.C(i - 1)
            self.curve.make_curve(-135, STEP)
            self.D(i - 1)


if __name__ == '__main__':
    COLOR = ['#000', '#fff']
    SIZE_X = 700
    SIZE_Y = 600
    STEP = 6
    root = Tk()
    root.title('Serpin curve')

    hello_field = Canvas(root, width=SIZE_X, height=SIZE_Y, bg=COLOR[1])
    hello_field.pack()

    text_for_user = Label(hello_field, text="Put the level of curve:", bg=COLOR[1], font="Arial 20")
    text_for_user.place(relx=.5, rely=.3, anchor="c")
    level = IntVar()
    level_entry = Entry(hello_field, textvariable=level)
    level_entry.place(relx=.5, rely=.4, anchor="c")

    def submit():
        hello_field.pack_forget()
        FIELD = Canvas(root, width=SIZE_X, height=SIZE_Y, bg=COLOR[1])
        FIELD.pack()
        Serpin(Curve(FIELD)).doit(get_level())

    def get_level():
        return level.get()

    level_button = Button(text="Submit", command=submit)
    level_button.place(relx=.5, rely=.6, anchor="c")
    root.mainloop()
