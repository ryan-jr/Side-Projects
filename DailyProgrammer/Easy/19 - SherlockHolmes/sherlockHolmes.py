# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:41:13 2018

@author: rjr
"""

excludeList = ["I. A Scandal in Bohemia", "II. The Red-headed League", "III. A Case of Identity",
    "IV. The Boscombe Valley Mystery", "V. The Five Orange Pips", "VI. The Man with the Twisted Lip",
    "VII. The Adventure of the Blue Carbuncle", "VIII. The Adventure of the Speckled Band", 
    "IX. The Adventure of the Engineer's Thumb", "X. The Adventure of the Noble Bachelor",
    "XI. The Adventure of the Beryl Coronet", "XII. The Adventure of the Copper Beeches", "ADVENTURE"]

lookup = "*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
lookup2 = "*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
y = 0

with open("SherlockHolmes.txt", "r") as f:
        x = f.readlines()
        z = list(str(x))
        for i in z:
            y += 1
            if i == "*":
                print("Character number:", y)

   
    
    
    
    
    
"""

# Counters for lines that I want to exclude from the char count


             
"""