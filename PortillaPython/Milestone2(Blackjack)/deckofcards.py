# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:42:04 2018

@author: rjr
"""


import random

class Card(object):
    """Class to create cards to be used in our game of Blackjack.
    
    
    
    Methods:
        show: prints the value and suit of the card
        showValue: returns the value of the card
        
    """
    
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))
        
    def showValue(self):
        return self.value
    
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(2, 14):
                self.cards.append(Card(s, v))
           
    def show(self):
        for c in self.cards:
            c.show()
            
            
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, - 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, ctr = 0):
        self.hand = []
        self.values = []
        self.ctr = 0
        
    def draw(self, deck):
        i = deck.drawCard()
        self.hand.append(i)
        
        return self
        
    def showHand(self):
        for card in self.hand:
            card.show()
            
    def getValues(self):
        if self.ctr == 0:
            self.ctr += 2
            for i in self.hand:
                self.values.append(i.showValue())
        else:
            self.values.append(self.hand[-1].showValue())
            
        return sum(self.values)
         
            
            
            
            
class Player2(object):
    def __init__(self, ctr = 0):
        self.hand = []
        self.values = []
        self.ctr = 0
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
        
    def showHand(self):
        for card in self.hand:
            card.show()
            
    def getValues(self):
        if self.ctr == 0:
            self.ctr += 2
            for i in self.hand:
                self.values.append(i.showValue())
        else:
            self.values.append(self.hand[-1].showValue())
            
        return sum(self.values)

    