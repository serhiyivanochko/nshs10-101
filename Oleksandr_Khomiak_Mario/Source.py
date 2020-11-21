from tkinter import*
win = Tk()

canvas = Canvas(width=1000, height=600)
canvas.pack()

bot_x = 200
bot_y = 550
dx = 10
bot_width = 50
bot_height = 50
player_y1 = 550
player_y2 = 600
player_x1 = 0
player_x2 = 50
player = canvas.create_rectangle(player_x1, player_y1, player_x2, player_y2, fill="red")
block_x1 = 500
block_x2 = 550
block_y1 = 500
block_y2 = 450
block = canvas.create_rectangle(block_x1, block_y1, block_x2, block_y2, fill="green")
bot_2 = canvas.create_rectangle(bot_x, bot_y, bot_x + bot_width, bot_y + bot_height, fill="green")
obstacle1 = canvas.create_rectangle(block_x1-100,block_y2+100,block_x2,block_y2+150,fill = "yellow")
obstacle2 = canvas.create_rectangle(player_x1+100,block_y2+100,player_x2 +100,block_y2+150,fill = "yellow")
finish = canvas.create_polygon((840, 475), (890, 450), (890, 500),fill='orange', outline='black')
finish2 = canvas.create_rectangle(890,600,900,450,fill = "orange", outline = "black")




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
    coin = canvas.create_oval(505, 410, 545, 370, fill="yellow")
def leftKey(event):
    global player
    global player_x1
    global player_x2
    global player_y1
    global player_y2
    player_x1 = player_x1 - 10
    player_x2 = player_x2 - 10
    canvas.coords(player,player_x1,player_y1, player_x2, player_y2)
    create_block()
    victory()
def rightKey(event):
    global player
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_x1 = player_x1 + 10
    player_x2 = player_x2 + 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()
    victory()
def upKey(event):
    global player
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_y1 = player_y1 - 10
    player_y2 = player_y2 - 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()
    victory()
def downKey(event):
    global player
    global player_y1
    global player_y2
    global player_x1
    global player_x2
    player_y1 = player_y1 + 10
    player_y2 = player_y2 + 10
    canvas.coords(player, player_x1, player_y1, player_x2, player_y2)
    create_block()
    victory()

def move_bot():
    global bot_x
    global dx

    bot_x = bot_x + dx
    if bot_x + bot_width <= 200 or bot_x >= 350:
        dx = -dx
    canvas.coords(bot_2, bot_x, bot_y, bot_x + bot_width, bot_y + bot_height)
    win.after(40, move_bot)

def victory():
    if player_x1 >= 890:
        print("you win!!!")


move_bot()
victory()
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