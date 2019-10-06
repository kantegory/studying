from tkinter import *


def wipes(c, x1, y1, x2, y2, x3, y3, level):
    if level > 0:
        c.create_line(x1, y1, x2, y2, fill=COLOR[0])
        c.create_line(x2, y2, x3, y3, fill=COLOR[0])
        c.create_line(x3, y3, x1, y1, fill=COLOR[0])
        nx1 = x1 + (x2 - x1) / 2
        ny1 = y1 + (y2 - y1) / 2
        nx2 = x2 + (x3 - x2) / 2
        ny2 = y2 + (y3 - y2) / 2
        nx3 = x3 + (x1 - x3) / 2
        ny3 = y3 + (y1 - y3) / 2
        wipes(c, x1, y1, nx1, ny1, nx3, ny3, level - 1)
        wipes(c, x2, y2, nx2, ny2, nx1, ny1, level - 1)
        wipes(c, x3, y3, nx3, ny3, nx2, ny2, level - 1)


if __name__ == "__main__":
    SIZE_X = 700
    SIZE_Y = 600
    COLOR = ['#000', '#fff']
    root = Tk()
    root.title("Serpin wipes")
    hello_field = Canvas(root, width=SIZE_X, height=SIZE_Y, bg=COLOR[1])
    hello_field.pack()

    text_for_user = Label(hello_field, text="Put the level of triangle:", bg=COLOR[1], font="Arial 20")
    text_for_user.place(relx=.5, rely=.3, anchor="c")
    level = IntVar()
    level_entry = Entry(hello_field, textvariable=level)
    level_entry.place(relx=.5, rely=.4, anchor="c")


    def submit():
        hello_field.pack_forget()
        FIELD = Canvas(root, width=SIZE_X, height=SIZE_Y, bg=COLOR[1])
        FIELD.pack()
        wipes(FIELD, SIZE_X / 2, 10, 10, SIZE_Y - 10, SIZE_X - 10, SIZE_Y - 10, get_level())


    def get_level():
        return level.get()


    level_button = Button(text="Submit", command=submit)
    level_button.place(relx=.5, rely=.6, anchor="c")
    root.mainloop()
