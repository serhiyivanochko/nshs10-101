from tkinter import *

main = Tk()


def roll():
    global rect_x
    global rect_y
    global rect
    global rect_width
    global rect_height
    global px


rect_x = 50
rect_y = 540
rect_width = 50
rect_height = 50
px = 7

canvas = Canvas(width=1000, height=600, bg="black")
canvas.pack()
rect = canvas.create_rectangle(rect_x, rect_y, rect_x + rect_width, rect_y + rect_height, fill="green")

def leftKey(event):
    global rect_x
    rect_x = rect_x - px
    canvas.coords(rect, rect_x, rect_y, rect_x + rect_width, rect_y + rect_height)


def rightKey(event):
    global rect_x
    rect_x = rect_x + px
    canvas.coords(rect, rect_x, rect_y, rect_x + rect_width, rect_y + rect_height)


main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)
main.mainloop()
