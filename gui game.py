from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
root.geometry('400x400')


row1 = Frame(root)
row1.pack(expand=True, fill=BOTH)
row2 = Frame(root)
row2.pack(expand=True, fill=BOTH)
row3 = Frame(root)
row3.pack(expand=True, fill=BOTH)
player_turn = Label(root, text="Player 1 start the game")
player_turn.pack(side=LEFT)

default = ['1','2','3','4','5','6','7','8','9']
board = ['1','2','3','4','5','6','7','8','9']


def player_one_entry(square):
    if square['text'] == "X" or square['text'] == "O":
        print("You can't go there")
        return
    square.config(text="X")
    if iswinner("X"):
        player_turn.config(text="Player 1 Wins!!")
        return
    player2_set()


def player_two_entry(square):
    if square['text'] == "X" or square['text'] == "O":
        print("You can't go there")
        return
    square.config(text="O")
    if iswinner("O"):
        player_turn.config(text="Player 2 Wins!!")
        return
    player1_set()


square1 = Button(row1, text=1)
square1.pack(side=LEFT, expand=True, fill=BOTH)
square2 = Button(row1, text=2)
square2.pack(side=LEFT, expand=True, fill=BOTH)
square3 = Button(row1, text=3)
square3.pack(side=LEFT, expand=True, fill=BOTH)
square4 = Button(row2, text=4)
square4.pack(side=LEFT, expand=True, fill=BOTH)
square5 = Button(row2, text=5)
square5.pack(side=LEFT, expand=True, fill=BOTH)
square6 = Button(row2, text=6)
square6.pack(side=LEFT, expand=True, fill=BOTH)
square7 = Button(row3, text=7)
square7.pack(side=LEFT, expand=True, fill=BOTH)
square8 = Button(row3, text=8)
square8.pack(side=LEFT, expand=True, fill=BOTH)
square9 = Button(row3, text=9)
square9.pack(side=LEFT, expand=True, fill=BOTH)


def clearing():
    square1.config(text=1)
    square2.config(text=2)
    square3.config(text=3)
    square4.config(text=4)
    square5.config(text=5)
    square6.config(text=6)
    square7.config(text=7)
    square8.config(text=8)
    square9.config(text=9)
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


def playing_game():
    player1_set()
    if iswinner("X"):
        player_turn.config(text="Player 1 Wins!!")
        return
    elif iswinner("O"):
        player_turn.config(text="Player 2 Wins!!")
        return
    player_turn.config(text="Player 2 your turn")
    print("1")


playing_game()


root.mainloop()


