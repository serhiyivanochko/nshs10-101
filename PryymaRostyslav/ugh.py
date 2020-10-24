from tkinter import *
window = Tk()

dx = 10
player_x = 250
player_y = 200
isBig = False
player_height = 50
player_width = 50
mushroom_x = 400
mushroom_y = 200
mushroom_height = 50
mushroom_width = 50
canvas = Canvas(window, width=600, height=500, bg="blue")
canvas.pack()
player = canvas.create_oval(player_x, player_y, player_x + player_width, player_y + player_height, fill="green")
mushroom = canvas.create_rectangle(mushroom_x, mushroom_y, mushroom_x + mushroom_height, mushroom_y + mushroom_width, fill="red")

def left(event):
    global player_x
    player_x = player_x - dx
    canvas.coords(player, player_x, player_y, player_x + player_width, player_y + player_height)

def right(event):
    global isBig
    global player_x
    global player_y
    global mushroom_x
    global mushroom_y
    global player_height
    global player_width
    player_x = player_x + dx
    canvas.coords(player, player_x, player_y, player_x + player_width, player_y + player_height)
    if player_x >= mushroom_x and isBig is False:
        isBig = True
        canvas.delete(mushroom)
        player_height = player_height + 50
        player_width = player_width + 50

def jump(event):
    global player_y
    player_y = player_y - player_height
    canvas.coords(player, player_x, player_y, player_x + player_width, player_y + player_height)







window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<space>', jump)
window.mainloop()