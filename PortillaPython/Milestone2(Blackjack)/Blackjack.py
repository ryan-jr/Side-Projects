# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:30:11 2017

@author: rjr
"""

"""
Create a text based blackjack/21 game
Must be one player versus and automated dealer
The player can stand/hit
The player must be able to pick the betting amount
You need to keep track of the players total money
You need to alert the player of wins, losses, busts, etc...

# Let's extend it to play 100 times, and after 100 times calculate win %
"""

from blackjackcards import Blackjackcards

def keepPlaying(q):
    q = input("Would you like to keep playing (Y or N): ")
    print(q)
    return q









q = ""
cardCtr = 0


while q != "N" or q != "n":
    if q == "N" or q == "n":
        print("Exiting")
        break
    elif cardCtr >= 21:
       q = keepPlaying(q)
    
    cardCtr += 1
    

