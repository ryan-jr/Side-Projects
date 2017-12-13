# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:56:14 2017

@author: rjr
"""

import random

class Blackjackcards(object):
    
    cards = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, 
             "9":9, "10":10, "J":11, "Q":12, "K":13}
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    
    
    def __init__(self):
        print("Cards made!")
        print(self.cards)
    
    def deal(self):
        print(random.choice(list(self.suits)))
        card1 = random.choice(list(self.cards))
        print(card1)
        print(random.choice(list(self.suits)))
        card2 = random.choice(list(self.cards))
        print(card2)
        
        
        cardAmt = self.cards[card1] + self.cards[card2]
        return cardAmt
    
    def hit(self):
        pass
    
    def stay(self):
        pass
        
  

class Money(object):
    
    startingAmount = 100
    houseBet = 5
    
    def __init__(self):
        pass
    
    def add(self, amt):
        pass
    
    def subtract(self, amt):
        pass
    
    def displayAmount(self, amt):
        pass
 
