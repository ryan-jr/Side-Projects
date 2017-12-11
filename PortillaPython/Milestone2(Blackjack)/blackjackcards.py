# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:56:14 2017

@author: rjr
"""

class Blackjackcards(object):
    
    cards = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
             "10":10, "J":11, "Q":12, "K":13}
    suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
    cardAmt = 0
    
    def __init__(self):
        print("Cards made!")
        print(self.cards)
    
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
    
