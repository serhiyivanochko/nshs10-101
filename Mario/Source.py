from tkinter import *
win = Tk()

def move_bot1():
    global bot1_x
    global dx
    bot1_x = bot1_x + dx
    if bot1_x + 50 == 400 or bot1_x <= 20:
        dx = -dx
    canvas.coords(bot1, bot1_x, 300, bot1_x + 50, 350)
    win.after(40, move_bot1)

bot1_x = 50
dx = 10

canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(500, 500, 550, 550, fill="red")
bot1 = canvas.create_rectangle(bot1_x, 300, bot1_x+50, 350, fill="green")

move_bot1()

win.mainloop()