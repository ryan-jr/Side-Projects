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

# TODO: 3.  Why is quitting after hitting
# TODO: 4.  Why aren't card totals summing properly?
def newDeck():
    """Function to create a new deck of cards
    
    Args:
        N/A
    
    Returns: 
        deck: A newly shuffled deck of cards from the deckofcards class
        
    Raises:
        N/A
    
    """
    deck = deckofcards.Deck()
    deck.shuffle()
    
    return deck

def stayChoice(flag):
    """Determines the player's choice for staying or hitting
    
    Args:
        flag: A boolean value that was preset for the game/loop
    
    Returns:
        flag: A boolean value that is set for that game/loop
    
    Raises:
        N/A
    """
    flag = input("Would you like to stay or hit?(s/h):" )
    if flag == "s":
        return True
    else:
        return False
      
# Variable, stats, and deck initilization
stayFlag = False
playFlag = True

playerCashAmount = 100.00
dealerCashAmount = 100.00
betAmount = 5.00

bustCount = 0
winCount = 0
lossCount = 0

playAgain = "y"
ctr = 0

deck = newDeck()


while playFlag:
    ctr += 1
    
    if playerCashAmount < 5.00:
        print("Sorry you don't have enough!")
        break
    elif dealerCashAmount < 5.00:
        print("You beat the house!")
        break
    
    
    if playAgain  == "y":
        playFlag = True
        deck = newDeck()
                
        player = deckofcards.Player()
        dealer = deckofcards.Player2()
            
        player.draw(deck).draw(deck)
        player.showHand()
        playerCardTotal = player.getValues()
        print("Player has:", playerCardTotal) 

        print("")
        dealer.draw(deck).draw(deck)
        dealer.showHand()
        dealerCardTotal = dealer.getValues()
        print("Dealer has:", dealerCardTotal)
        playAgain = "n"
    else:
        playFlag = False
        break   
    
    # Draw case
    if playerCardTotal == 21 and dealerCardTotal == 21:
        print("It's a draw!")
    
    print("")
    
    # Dealer logic
    if dealerCardTotal < 18:
        dealer.draw(deck)
        print("Dealer draws")
        dealer.showHand()
        dealerCardTotal = dealer.getValues()
        print("Dealer has:", dealerCardTotal)
    elif dealerCardTotal > 21:
        print("Dealer loses!")
    else:
        print("Dealer stays with", dealerCardTotal)

    if dealerCardTotal > 21:
        print("Dealer has:", dealerCardTotal, " and loses.  YOU WIN!")
        playAgain = input("Would you like to play again?(y/n): ")
        winCount += 1
        dealerCashAmount -= betAmount
        playerCashAmount += betAmount
        
        pass
    else:
        print("You have:", playerCardTotal)
        stayFlag = stayChoice(stayFlag)
        
        # Player logic
        if stayFlag == False:
            player.draw(deck)
            print("Player draws")
            player.showHand()
            x = player.getValues()
            print("Player has:", playerCardTotal)
        else:
            print("Player stays with", playerCardTotal)
    
    if playerCardTotal > 21:
        print("Player loses")
        playAgain = input("Would you like to play again?(y/n): ")
        lossCount += 1
        playerCashAmount -= betAmount
        dealerCashAmount += betAmount
        print("You have:", playerCashAmount)
        continue
    
    if playerCardTotal < 21 and stayFlag == True:
        if dealerCardTotal > playerCardTotal:
            print("Player loses with:", playerCardTotal)
            playAgain = input("Would you like to play again?(y/n): ")
            lossCount += 1
            playerCashAmount -= betAmount
            dealerCashAmount += betAmount
            print("You have:", playerCashAmount)
        elif playerCardTotal > dealerCardTotal:
            print("Dealer loses with:", dealerCardTotal, "YOU WIN!")
            playAgain = input("Would you like to play again?(y/n): ")
            winCount += 1
            dealerCashAmount -= betAmount
            playerCashAmount += betAmount
        else:
            print("It's a tie!!!")
            playAgain = input("Would you like to play again?(y/n): ")

# Display score/statistics
print("")
print("Wins:", winCount)
print("Losses:", lossCount)
print("Amount:", playerCashAmount)
print()
print("After", ctr, " games you won an average of", playerCashAmount/ctr, "per hand")