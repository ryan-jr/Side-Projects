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

# while x <= 21 and stayFlag == False, ask player stay or hit
    # What does the computer do during this?
        # If the computer is <= 18, hit, otherwise stay
        # If the dealer busts, then it's an automatic player win
        # If the player busts it's an automatic player loss
        

import deckofcards


def dealerLogic(dealerCount):
    if dealerCount < 18:
        dealer.draw(deck)
        print("Dealer draws")
        dealer.showHand()
        dealerCount = dealer.getValues()
        print("Dealer has:", dealerCount)
    elif y > 21:
        print("Dealer loses!")
    else:
        print("Dealer stays with", dealerCount)
        dealer.showHand()

# Variable initialization
stayFlag = False
playFlag = True

playerAmount = 100.00
dealerAmount = 100.00

bustCount = 0
winCount = 0
lossCount = 0

# Deck and player/dealer calls to start the game
deck = deckofcards.Deck()
deck.shuffle()

player = deckofcards.Player()
dealer = deckofcards.Player2()

player.draw(deck).draw(deck)
player.showHand()
x = player.getValues()
print("Player has:", x) 

print("")
dealer.draw(deck).draw(deck)
dealer.showHand()
y = dealer.getValues()
print("Dealer has:", y) 

while playFlag:
    
    # Draw case
    if x == 21 and y == 21:
        print("It's a draw!")
    
    print("")
    
    # Dealer logic

        
    # Player logic
    if y < 18:
        player.draw(deck)
        print("Player draws")
        player.showHand()
        x = player.getValues()
        print("Player has:", x)
    elif y > 21:
        print("Player loses!")
    else:
        print("Player stays with", x)
        player.showHand()
    
    #playerChoice == input("Would you like to stay or hit?")

    if x >= 21:
        print("Player loses!")
        lossCount += 1
    elif y >= 21:
        print("Dealer loses!")
        winCount += 1
        
    playAgain = "y"# input("Would you like to play again?(y/n): ")
    if playAgain  == "y":
        playFlag = True
        deck = deckofcards.Deck()
        deck.shuffle()
        
        player = deckofcards.Player()
        dealer = deckofcards.Player2()
            
        player.draw(deck).draw(deck)
        player.showHand()
        x = player.getValues()
        print("Player has:", x) 
            
        print("")
        dealer.draw(deck).draw(deck)
        dealer.showHand()
        y = dealer.getValues()
        print("Dealer has:", y)
        
    else:
        playFlag = False
        break
    
    
print("Wins: ", winCount)
print("Losses: ", lossCount)
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
