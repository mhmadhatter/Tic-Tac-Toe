from tkinter import *
import time

root = Tk()
root.title("Tic Tac Toe")
root.geometry('300x300')


row1 = Frame(root)
row1.pack(expand=True, fill=BOTH)
row2 = Frame(root)
row2.pack(expand=True, fill=BOTH)
row3 = Frame(root)
row3.pack(expand=True, fill=BOTH)
player_turn = Label(root, text="Player 1 start the game")
player_turn.pack(side=LEFT)


def player_one_entry(square):
    if square['text'] == "X" or square['text'] == "O":
        player_turn.config(text="You can't go there")
        return
    square.config(text="X")
    if iswinner("X"):
        player_turn.config(text="Player 1 Wins!!")
        return
    player_turn.config(text="")
    istie()
    player2_set()


def player_two_entry(square):
    if square['text'] == "X" or square['text'] == "O":
        player_turn.config(text="You can't go there")
        return
    square.config(text="O")
    if iswinner("O"):
        player_turn.config(text="Player 2 Wins!!")
        return
    player_turn.config(text="")
    istie()
    player1_set()


square1 = Button(row1, text=" ", width=2, height=2)
square1.pack(side=LEFT, expand=True, fill=BOTH)
square2 = Button(row1, text=" ", width=2, height=2)
square2.pack(side=LEFT, expand=True, fill=BOTH)
square3 = Button(row1, text=" ", width=2, height=2)
square3.pack(side=LEFT, expand=True, fill=BOTH)
square4 = Button(row2, text=" ", width=2, height=2)
square4.pack(side=LEFT, expand=True, fill=BOTH)
square5 = Button(row2, text=" ", width=2, height=2)
square5.pack(side=LEFT, expand=True, fill=BOTH)
square6 = Button(row2, text=" ", width=2, height=2)
square6.pack(side=LEFT, expand=True, fill=BOTH)
square7 = Button(row3, text=" ", width=2, height=2)
square7.pack(side=LEFT, expand=True, fill=BOTH)
square8 = Button(row3, text=" ", width=2, height=2)
square8.pack(side=LEFT, expand=True, fill=BOTH)
square9 = Button(row3, text=" ", width=2, height=2)
square9.pack(side=LEFT, expand=True, fill=BOTH)


def clearing():
    square1.config(text=" ")
    square2.config(text=" ")
    square3.config(text=" ")
    square4.config(text=" ")
    square5.config(text=" ")
    square6.config(text=" ")
    square7.config(text=" ")
    square8.config(text=" ")
    square9.config(text=" ")
    player_turn.config(text="Player 1 start the game")


clear = Button(root, text="Clear", command=lambda: clearing())
clear.pack(side=RIGHT)


def player1_set():
    square1.config(command=lambda: player_one_entry(square1))
    square2.config(command=lambda: player_one_entry(square2))
    square3.config(command=lambda: player_one_entry(square3))
    square4.config(command=lambda: player_one_entry(square4))
    square5.config(command=lambda: player_one_entry(square5))
    square6.config(command=lambda: player_one_entry(square6))
    square7.config(command=lambda: player_one_entry(square7))
    square8.config(command=lambda: player_one_entry(square8))
    square9.config(command=lambda: player_one_entry(square9))


def player2_set():
    square1.config(command=lambda: player_two_entry(square1))
    square2.config(command=lambda: player_two_entry(square2))
    square3.config(command=lambda: player_two_entry(square3))
    square4.config(command=lambda: player_two_entry(square4))
    square5.config(command=lambda: player_two_entry(square5))
    square6.config(command=lambda: player_two_entry(square6))
    square7.config(command=lambda: player_two_entry(square7))
    square8.config(command=lambda: player_two_entry(square8))
    square9.config(command=lambda: player_two_entry(square9))


def iswinner(le):
    return((square1['text'] == le and square2['text'] == le and square3['text'] == le) or
           (square4['text'] == le and square5['text'] == le and square6['text'] == le) or
           (square7['text'] == le and square8['text'] == le and square9['text'] == le) or
           (square1['text'] == le and square4['text'] == le and square7['text'] == le) or
           (square2['text'] == le and square5['text'] == le and square8['text'] == le) or
           (square3['text'] == le and square6['text'] == le and square9['text'] == le) or
           (square1['text'] == le and square5['text'] == le and square9['text'] == le) or
           (square3['text'] == le and square5['text'] == le and square7['text'] == le))


def istie():
    if (square1['text'] == "X" or square1['text'] == "O"):
        if (square2['text'] == "X" or square2['text'] == "O"):
            if (square3['text'] == "X" or square3['text'] == "O"):
                if (square4['text'] == "X" or square4['text'] == "O"):
                    if (square5['text'] == "X" or square5['text'] == "O"):
                        if (square6['text'] == "X" or square6['text'] == "O"):
                            if (square7['text'] == "X" or square7['text'] == "O"):
                                if (square8['text'] == "X" or square8['text'] == "O"):
                                    if (square9['text'] == "X" or square9['text'] == "O"):
                                        player_turn.config(text="Tie Game")
                                        return


player1_set()


root.mainloop()
