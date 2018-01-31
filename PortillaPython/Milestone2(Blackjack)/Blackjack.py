# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:30:11 2017

@author: rjr
"""

"""
Create a text based blackjack/21 game
Must be one player versus an automated dealer
The player can stand/hit
The player must be able to pick the betting amount
You need to keep track of the players total money
You need to alert the player of wins, losses, busts, etc...

# Let's extend it to play 100 times, and after 100 times calculate win %
"""

import deckofcards

deck = deckofcards.Deck()
deck.shuffle()

player = deckofcards.Player()
dealer = deckofcards.Player2()

player.draw(deck).draw(deck)
player.showHand()
x = player.getValues()
print("Player has:", x) 




dealer.draw(deck).draw(deck)
dealer.showHand()
y = dealer.getValues()
print("Dealer has:", y) 

"""
def keepPlaying(data):
    data = input("Keep playing Y or N?: ")
    return data




# Tracking variables
userInput = ""
cardCtr = 0
playerCardCtr = 0
dealerCardCtr = 0


# While loop to play the game
while userInput != "N" or userInput != "n":
    if userInput == "N" or userInput == "n":
        print("Exiting")
        break
    elif cardCtr >= 21:
       userInput = keepPlaying(userInput)
       dealerAmt = dealer.deal()
       playerAmt = player.deal()
       print("Dealer amount: ", dealerAmt)
       print("Player amount: ", playerAmt)
       
    
    cardCtr += 1
    print(cardCtr)
    
"""
