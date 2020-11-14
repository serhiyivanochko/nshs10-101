from tkinter import*
win = Tk()

canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(500, 500, 550, 550, fill="red")

player_y1 = 500
player_y2 = 550
player_x1 = 500
player_x2 = 550
player = canvas.create_rectangle(player_x1, player_y1, player_x2, player_y2, fill="red")
block_x1 = 500
block_x2 = 550
block_y1 = 470
block_y2 = 420
block = canvas.create_rectangle(block_x1, block_y1, block_x2, block_y2, fill="green")


def create_block():
    global coin
    global block_x1
    global block_x2
    global block_y1
    global block_y2
    global player_x1
    global player_x2
    global player_y1
    global player_y2
    if block_y1 >= player_y1 and block_y2 <= player_y2 and block_x1 <= player_x2 and block_x2 >= player_x1:
        create_coin()

def create_coin():
    global coin
    coin = canvas.create_oval(500, 420, 550, 370, fill="yellow")
def leftKey(event):
    global player_x1
    global player_x2
    global player_y1
    global player_y2
    player_x1 = player_x1 - 10
    player_x2 = player_x2 - 10
    canvas.coords(player,player_x1,player_y1, player_x2, player_y2)
    create_block()
def rightKey(event):
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_x1 = player_x1 + 10
    player_x2 = player_x2 + 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()
def upKey(event):
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_y1 = player_y1 - 10
    player_y2 = player_y2 - 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()
def downKey(event):
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_y1 = player_y1 + 10
    player_y2 = player_y2 + 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()

win.bind('<Left>', leftKey)
win.bind('<Right>', rightKey)
win.bind('<Up>', upKey)
win.bind('<Down>', downKey)

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