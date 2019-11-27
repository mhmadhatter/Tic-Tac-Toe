import time, os
import sys


def draw_board(board):
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")


default = ['1','2','3','4','5','6','7','8','9']
board = ['1','2','3','4','5','6','7','8','9']

draw_board(board)

def player_one_entry(square):
    if board[square] == "X" or board[square] == "O":
        print("You can't go there")
        return
    board[square] = "X"


def player_two_entry(square):
    if board[square] == "X" or board[square] == "O":
        print("You can't go there")
        return
    board[square] = "O"


def iswinner(bo, le):
    return((bo[0] == le and bo[1] == le and bo[2] == le) or
           (bo[3] == le and bo[4] == le and bo[5] == le) or
           (bo[6] == le and bo[7] == le and bo[8] == le) or
           (bo[0] == le and bo[3] == le and bo[6] == le) or
           (bo[1] == le and bo[4] == le and bo[7] == le) or
           (bo[2] == le and bo[5] == le and bo[8] == le) or
           (bo[0] == le and bo[4] == le and bo[8] == le) or
           (bo[2] == le and bo[4] == le and bo[6] == le))


def tiegame(bo, default):
    diff = list(set(default) - set(bo))
    if len(diff) == 9:
        print("Tie Game")
        return False

def askmove():
    player1 = input("Player 1 chose your square: ")
    if int(player1) > 9 or int(player1) < 1:
        print("That is not a valid square")
        return
    player_one_entry(int(player1) - 1)
    draw_board(board)
    if iswinner(board, "X"):
        return
    player2 = input("Player 2 chose your square: ")
    if int(player2) > 9 or int(player2) < 1:
        print("That is not a valid square")
        return
    player_two_entry(int(player2) - 1)
    draw_board(board)

while True:
    askmove()
    winner1 = iswinner(board, "X")
    winner2 = iswinner(board, "O")
    if winner1:
        print("Player 1 Wins!")
        break
    elif winner2:
        print("Player 2 Wins!")
        break
    tie = tiegame(board, default)
    if tie == False:
        break

