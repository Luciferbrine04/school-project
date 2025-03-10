from tkinter import *
from PIL import ImageTk, Image
import time

def game(player1, mainwindow):
    window = Toplevel(mainwindow)
    window.geometry("600x300")
    p1 = PhotoImage(file = './turtle/assets/turtle1.png')
    window.iconphoto(False, p1)
    window.title("Turtle Game | VVLC")
    global winner, loser, player1pos, player2pos
    player1pos = 0
    player2pos = 0
    winner = None
    loser = None

    def gameover(winner, loser):
        winimg = Image.open("./turtle/assets/winner.png")
        #winimg = img2.resize((200,50), Image.ANTIALIAS)
        winimg = ImageTk.PhotoImage(winimg)
        canvas.create_image(300, 150, image=winimg)

    def save():
        savebutton["state"] = "disabled"

    def exit():
        window.destroy()

    def keypress(event):
        global player1pos, player2pos, winner, loser
        if winner == None:
            if event.char == "z":
                canvas.move(player1, 10, 0)
                player1pos += 2
            elif event.char == "m":
                canvas.move(player2, 10, 0)
                player2pos += 2
            if player1pos == 100:
                print("Player 1 Wins")
                winner = 1
                loser = 2
                savebutton.pack()
                exitbutton.pack()
                gameover(winner, loser)
            elif player2pos == 100:
                print("Player 2 Wins")
                winner = 2
                loser = 1
                savebutton.pack()
                exitbutton.pack()
                gameover(winner, loser)

    #global button2
    savebutton =  Button(window, text="Save", command=save)
    #global button1
    exitbutton =  Button(window, text="EXIT", command=exit)

    canvas = Canvas(window, width = 500, height = 250)
    canvas.pack()
    img1 = Image.open("./turtle/assets/turtle2.png")
    img1 = img1.resize((50,50), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("./turtle/assets/turtle3.png")
    img2 = img2.resize((50,50), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    player1 = canvas.create_image(0, 80, image=img1)
    player2 = canvas.create_image(0, 150, image=img2)
    canvas.create_line(30, 30, 30, 200, fill="red")

    window.bind("<Key>", keypress)

    window.mainloop()