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

"""       
import deckofcards

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
        print("flag was s, returning true")
    else:
        print("flag was h, returning false")
        return False
    
def betting(amountAlreadyBet, playerCashAmount):
    """Function to determine the bet amount that the player bets
    
    Args:
        amountAlreadyBet: How much the player has already bet
        playerCashAmount: The amount of $$$ a player has in the bank
        
    Returns:
        betAmount: The amount the player has chosen to bet
        
    Raises:
        N/A
        
    """
    print("Bet amounts are in $5.00 increments")
    print("")

    betAmount = input("How much do you want to bet")
    betAmount = float(betAmount)
    
    if betAmount < 5.00:
      print("Enter a higher bet amount!")
      betting(amountAlreadyBet, playerCashAmount)
    elif float(betAmount) > float(playerCashAmount):
      print("You don't have that much to bet!")
      betting(amountAlreadyBet, playerCashAmount)
    else:
        return float(betAmount + amountAlreadyBet)
    
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
    
    # Stopping the game if there's not enough bank
    if playerCashAmount < 5.00:
        print("Sorry you don't have enough!")
        break
    elif dealerCashAmount < 5.00:
        print("You beat the house!")
        break
    
    # Starting if the player wants a new game
    if playAgain  == "y":
        ctr += 1
        playFlag = True
        deck = newDeck()
        betAmount = 5.00
                
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
        continue
    else:
        print("You have:", playerCardTotal)
        betAmount = betting(betAmount, playerCashAmount)
        stayFlag = stayChoice(stayFlag)
        
        # Player logic
        if stayFlag == False:
            player.draw(deck)
            print("Player draws")
            player.showHand()
            playerCardTotal = player.getValues()
            print("Player has:", playerCardTotal)
        else:
            print("Player stays with", playerCardTotal)
    
    # Bust logic
    if playerCardTotal > 21:
        print("Player loses")
        playAgain = input("Would you like to play again?(y/n): ")
        lossCount += 1
        playerCashAmount -= betAmount
        dealerCashAmount += betAmount
        print("You have:", playerCashAmount)
        continue
    
    # Checking other cases
    if playerCardTotal <= 21:
        if dealerCardTotal > playerCardTotal:
            print("Player loses with:", playerCardTotal)
            playAgain = input("Would you like to play again?(y/n): ")
            lossCount += 1
            playerCashAmount -= betAmount
            dealerCashAmount += betAmount
            print("You have:", playerCashAmount)
            continue
        elif playerCardTotal > dealerCardTotal:
            print("Dealer loses with:", dealerCardTotal, "YOU WIN!")
            playAgain = input("Would you like to play again?(y/n): ")
            winCount += 1
            dealerCashAmount -= betAmount
            playerCashAmount += betAmount
            continue           
        else:
            print("It's a tie!!!")
            print("You have:", playerCashAmount)
            playAgain = input("Would you like to play again?(y/n): ")


# Display score/statistics at the end
print("Player card total:", playerCardTotal, "Dealer card total:", dealerCardTotal)
print("")
print("Wins:", winCount)
print("Losses:", lossCount)
print("Amount:", playerCashAmount)
print()
print("After", ctr, " games you won an average of", playerCashAmount/ctr, "per hand")