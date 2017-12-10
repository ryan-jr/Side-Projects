# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:18:27 2017

@author: rjr
"""

# Tic Tac Toe game

"""
2 players should be able to play the game(at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then 
place a symbol on the board

"""

# Step 1: Accept Player input
    #A.  Construct a while loop/counter to determine who's turn it is
    #B.  Construct a function to determine if they put in correct input
    #       (If not, go back through the loop)
    #    1B.  Will need to be extended later to check and see if a square
    #         Has been taken.  
# Step 2: Create/Draw a blank board(lists!)
# Step 3: Have player input accepted on the board
# Step 4: Check for win conditions

def winCheck(win, board):
    
    if(board[0] == "X" and board[1] == "X" and board[2] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[3] == "X" and board[4] == "X" and board[5] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[6] == "X" and board[7] == "X" and board[8] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[0] == "X" and board[3] == "X" and board[6] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[1] == "X" and board[4] == "X" and board[7] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[2] == "X" and board[5] == "X" and board[8] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[0] == "X" and board[4] == "X" and board[8] == "X"):
        print("X wins!")
        return (True, board)
    elif(board[2] == "X" and board[4] == "X" and board[6] == "X"):
        print("X wins!")
        return (True, board)
    ###
    if(board[0] == "O" and board[1] == "O" and board[2] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[3] == "O" and board[4] == "O" and board[5] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[6] == "O" and board[7] == "O" and board[8] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[0] == "O" and board[3] == "O" and board[6] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[1] == "O" and board[4] == "O" and board[7] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[2] == "O" and board[5] == "O" and board[8] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[0] == "O" and board[4] == "O" and board[8] == "O"):
        print("O wins!")
        return (True, board)
    elif(board[2] == "O" and board[4] == "O" and board[6] == "O"):
        print("O wins!")
        return (True, board)
    return (False, board)


def inputValidation(move, square):
    """
    Accepts user input as a string, converts it to an int.  
    Checks the int to make sure the move is valid.
    TODO: Input validation for string versus int
    """
    square = int(square)
    if(square > 9 or square <= 0):
        print("Enter a valid move")
        return False
    elif(board[square - 1] == "X" or board[square - 1] == "O"):
        print("That square is already taken!")
        return False
    else:
        print("Valid move!")
        printBoard(move, square)
        return True
    

def printBoard(move=1, square=1):
    """
    Accepts input after validation, updates the board, and prints out the updated board
    """
    board[square - 1] = move
    print(board[0], end="")  
    print(" |" * 1, end="")
    print(board[1], end="")
    print("  |" * 1, end="")
    print(board[2])
    print("-" * 10)
    print(board[3], end="")
    print("  |" * 1, end="")
    print(board[4], end="")
    print("   |" * 1, end="")
    print(board[5])
    print("-" * 10)
    print(board[6], end="")
    print("  |" * 1, end="")
    print(board[7], end="")
    print("   |" * 1, end="")
    print(board[8], end="")

ctr = 1
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = False

print("Player 1 is X, Player 2 is O")
printBoard()

while(ctr <= 9 and win == False):
    if(ctr % 2 == 0):
        userInput = input("Player 2(O), input your move: ")
        data = inputValidation("O", userInput)
        if(data == True):
            print()
        else:
            ctr -= 1
    else:
        userInput = input("Player 1(X), input your move: ")
        data = inputValidation("X", userInput)
        if(data == True):
            print()
        else:
            ctr -= 1
    ctr += 1
    (win, board) = winCheck(win, board)
    print(ctr)