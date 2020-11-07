from tkinter import *
win = Tk()

def move_bot1():
    global bot1_x
    global dx
    bot1_x = bot1_x + dx
    if bot1_x + 50 == 400 or bot1_x <= 20:
        dx = -dx
    canvas.coords(bot1, bot1_x, 500, bot1_x + 50, 550)
    win.after(40, move_bot1)

def move_player(event):
    global player_x
    global player_x2
    global px
    global player_y
    global player_y2
    global py
    global cx
    global big_boost

    if event.keysym == 'Left':
        player_x = player_x - px
        player_x2 = player_x2 - px
    if event.keysym == 'Right':
        player_x = player_x + px
        player_x2 = player_x2 + px
    if event.keysym == 'Up':
        jump_up()

    if player_x + 50 >= cx or player_x == cx + 20:
        canvas.delete(coin)
    big = canvas.coords(big_boost)
    if len(big) > 0:
        if (player_x + 50 <= big[0] + px and player_x + 50 >= big[0] - px) or (player_x >= big[2] - px and player_x <= big[2] + px):
            canvas.delete(big_boost)
            player_x = player_x - 20
            player_y = player_y - 20
    canvas.coords(player, player_x, player_y, player_x2, player_y2)

def sit_player(event):
    global player_y
    global player_y2
    y = player_y
    sit = (player_y2 - player_y)/2
    if event.keysym == 'Down' and player_y < y + sit:
        player_y = player_y + sit
    canvas.coords(player, player_x, player_y, player_x2, player_y2)

def up_player(event):
    global player_y
    if event.keysym == 'Down':
        player_y = player_y - 25
    canvas.coords(player, player_x, player_y, player_x2, player_y2)

def jump_up():
    #global player_x
    global player_x2
    global player_y
    global player_y2
    global py
    #player_x = player_x + 5
    player_y = player_y - py
    player_y2 = player_y2 - py
    canvas.coords(player, player_x, player_y, player_x2, player_y2)
    if player_y <= 350:
        jump_down()
        return 0
    win.after(20, jump_up)

def jump_down():
    #global player_x
    global player_y
    global player_y2
    global player_x2
    global px
    global py
    #player_x = player_x + 5
    player_y = player_y + py
    player_y2 = player_y2 + py
    canvas.coords(player, player_x, player_y, player_x2, player_y2)
    if player_y2 >= 550:
        return 0
    win.after(20, jump_down)

bot1_x = 50
dx = 10
player_x = 500
player_x2 = 550
player_y = 500
player_y2 = 550
px = 20
py = 5
cx = 600
cy = 510


canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(player_x, player_y, player_x2, player_y2, fill="red")
gross = canvas.create_rectangle(0, 551, 1000, 600, fill="green")
bot1 = canvas.create_rectangle(bot1_x, 500, bot1_x+50, 550, fill="#ba12ac")
coin = canvas.create_oval(cx, cy, cx + 20, cy + 20, fill="#acab12")
big_boost = canvas.create_rectangle(400, 510, 430, 540, fill="#b1a1ca")

move_bot1()

win.bind_all('<Left>', move_player)
win.bind_all('<Right>', move_player)
win.bind_all('<Up>', move_player)
win.bind('<KeyRelease>', up_player)
win.bind('<KeyPress>', sit_player)
win.mainloop()