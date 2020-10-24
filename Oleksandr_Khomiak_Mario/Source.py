from tkinter import*
win = Tk()

canvas = Canvas(width=1000, height=600)
canvas.pack()

player = canvas.create_rectangle(500, 500, 550, 550, fill="red")


player_y = 500
player_x = 500
player = canvas.create_rectangle(player_x, player_y, player_x+50, player_y+50, fill="red")
block_x = 500
block_y = 470
block = canvas.create_rectangle(block_x,block_y,block_x+50,block_y-50,fill="green")

def create_block():
    global block_x
    global player_x
    if block_y >= player_y:
        if block_x >= player_x and block_x + 50 <= player_x +50:
            create_coin()



def create_coin():
    coin = canvas.create_oval(500, 420, 550, 370, fill="yellow")

win.mainloop()