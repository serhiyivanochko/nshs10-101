from tkinter import *

win = Tk()


ninga_2_width = 50
ninga_2_height = 50
i_move = 0
bot_2_x = 100
bot_2_y = 100
dx = 10
nx = 17
bot_2_width = 50
bot_2_height = 50
player_x = 200
player_y = 60
player_width = 50
player_height = 50
end_of_plane = 550

canvas = Canvas(width=1000, height=600)
canvas.pack()
bot_2 = canvas.create_rectangle(bot_2_x,bot_2_y,bot_2_x + bot_2_width,bot_2_y + bot_2_height, fill="green")
player = canvas.create_rectangle(player_x, player_y, player_x + player_width, player_y + player_height, fill="red")

#Test hard-core wall
test_wall_1 = canvas.create_rectangle(0,bot_2_y,50,bot_2_y + bot_2_height, fill="yellow")
test_wall_2 = canvas.create_rectangle(300,bot_2_y,350,bot_2_y + bot_2_height, fill="yellow")

def move_bot2():
    global bot_2_x
    global dx
    global i_move
    global ninga_2_x
    global ninga_2_y
    global player_y
    global ninga_turtl
    global  player_x
    global player_y

    bot_2_x = bot_2_x + dx
    if bot_2_x + bot_2_width <= 100 or bot_2_x >= 250:
        dx = -dx
    if player_y + player_height >= bot_2_y:
        if ((player_x <= bot_2_x and player_x <= bot_2_x + bot_2_width) or (player_x >= bot_2_x + bot_2_width and player_x + 1  <= bot_2_x + bot_2_width)) and i_move == 0 :
            i_move = 1
            canvas.delete(bot_2)
            ninga_2_x = bot_2_x
            ninga_2_y = bot_2_y
            player_y = player_y - 20
            player_y = player_y + 60
            player_x = player_x - 50
            canvas.coords(player, player_x, player_y, player_x + player_width, player_y + player_height)
            ninga_turtl = canvas.create_rectangle(ninga_2_x, ninga_2_y, ninga_2_x + ninga_2_width, ninga_2_y + ninga_2_height)
            ninga_turtles()

    canvas.coords(bot_2, bot_2_x, bot_2_y, bot_2_x + bot_2_width, bot_2_y + bot_2_height)
    win.after(40, move_bot2)
def ninga_turtles():
    global ninga_2_x
    global ninga_turtl
    global player_y
    if player_x + player_width == ninga_2_x and player_y == ninga_2_y:
        right_move_ninga_bot()
        print("r")
    elif player_x == ninga_2_x + ninga_2_width and player_y == ninga_2_y:
        left_move_ninga_bot()
        print("l")
    win.after(45, ninga_turtles)
def right_move_ninga_bot():
    global ninga_2_x
    global ninga_turtl
    global player_y
    ninga_2_x = ninga_2_x + nx
    canvas.coords(ninga_turtl, ninga_2_x, ninga_2_y, ninga_2_x + ninga_2_width, ninga_2_y + ninga_2_height)
    if ninga_2_y > end_of_plane:
        canvas.delete(ninga_turtl)
    win.after(45, right_move_ninga_bot)
def left_move_ninga_bot():
    global ninga_2_x
    global ninga_turtl
    global player_y
    global nx
    ninga_2_x = ninga_2_x - nx
    canvas.coords(ninga_turtl, ninga_2_x, ninga_2_y, ninga_2_x + ninga_2_width, ninga_2_y + ninga_2_height)
    if bot_2_x + bot_2_width <= 100 or bot_2_x >= 250:
        nx = -nx
    if ninga_2_y > end_of_plane:
        canvas.delete(ninga_turtl)
    win.after(45, left_move_ninga_bot)

move_bot2()

win.mainloop()

