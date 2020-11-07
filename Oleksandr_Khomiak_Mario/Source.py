from tkinter import*
win = Tk()

canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(500, 500, 550, 550, fill="red")

player_y1 = 500
player_y2 = player_y1 + 50
player_x1 = 500
player_x2 = player_x1 + 50
player = canvas.create_rectangle(player_x1, player_y1, player_x2, player_y2, fill="red")
block_x = 500
block_y = 470
block = canvas.create_rectangle(block_x,block_y,block_x+50,block_y-50,fill="green")

def create_block():
    global block_x
    global player_x
    if block_y >= player_y1:
        if block_x >= player_x1 and block_x + 50 <= player_x +50:
            create_coin()


def create_coin():
    coin = canvas.create_oval(500, 420, 550, 370, fill="yellow")
def leftKey(event):
    
    global player_x1
    global player_x2
    global player_y1
    global player_y2
    player_x1 = player_x1 - 50
    player_x2 = player_x2 - 50
    player_y1 = player_y1 - 50
    player_y2 = player_y2 - 50
def rightKey(event):

    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_x1 = player_x1 + 50
    player_x2 = player_x2 + 50
    player_y1 = player_y1 + 50
    player_y2 = player_y2 + 50


win.bind('<Left>', leftKey)
win.bind('<Right>', rightKey)

win.mainloop()

'''from tkinter import *

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()'''

'''from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()'''