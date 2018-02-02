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


def newDeck():
    deck = deckofcards.Deck()
    deck.shuffle()
    
    return deck

def playerChoice(flag):
    choice = input("Would you like to stay or hit?(s/h):" )
    if choice == "s":
        return flag
    else:
        flag = True
        return flag
    

    
# Variable initialization
stayFlag = False
playFlag = True

playerAmount = 100.00
dealerAmount = 100.00
betAmount = 5.00

bustCount = 0
winCount = 0
lossCount = 0

# Deck and player/dealer calls to start the game
deck = newDeck()

"""
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
"""
playAgain = "y"
ctr = 0
while playFlag and ctr <= 100:
    ctr += 1
    
    if playerAmount < 5.00:
        print("Sorry you don't have enough!")
        break
    elif dealerAmount < 5.00:
        print("You beat the house!")
    
    if playAgain  == "y" and playerAmount > 5.00 and dealerAmount > 5.00:
        playFlag = True
        deck = newDeck()
                
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
    
    # Draw case
    if x == 21 and y == 21:
        print("It's a draw!")
    
    print("")
    
    # Dealer logic
    if y < 18:
        dealer.draw(deck)
        print("Dealer draws")
        dealer.showHand()
        y = dealer.getValues()
        print("Dealer has:", y)
    elif y > 21:
        print("Dealer loses!")
    else:
        print("Dealer stays with", y)
        dealer.showHand()

    if y > 21:
        playAgain = "y" # input("Would you like to play again?(y/n): ")
        winCount += 1
        dealerAmount -= betAmount
        playerAmount += betAmount
        print("Dealer has:", dealerAmount)
        continue
        
    # Player logic
    if y <= 18 and stayFlag == False:
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
    
    if x > 21:
        playAgain = "y" # input("Would you like to play again?(y/n): ")
        lossCount += 1
        playerAmount -= betAmount
        dealerAmount += betAmount
        print("You have:", playerAmount)
        continue
        
    
    



print("Wins:", winCount)
print("Losses:", lossCount)
print("Amount:", playerAmount)




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
    
    
    
***
        
    if y >= 21:
        winCount += 1
        continue
    else: 
        pass
        # stayFlag == playerChoice(stayFlag)
    
"""
