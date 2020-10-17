from tkinter import *
win = Tk()

canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(500, 500, 550, 550, fill="red")
win.mainloop()