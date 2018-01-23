# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:14:25 2018

@author: rjr
"""

# Iterate over the lines of the file checking each of the words and seeing 
# if they contain the most common words in the dictionary, if they do, add that line 
# to a list

words = []
poetryWords = ["time", "light", "night", "long", "love", "man", "yes", "white", "world", "face", "air", "left", "black", "water", "head", "life", "day", "hand", "people", "wind",
"inside", "sea", "red", "things", "lost"]

with open("MostCommon.txt", "r") as f:
    x = f.readlines()
    
    
x = list(map(lambda s: s.strip(), x))


with open("poetry.txt", "r") as f:
    for line in f:
        if len(line) > 100:
            pass
        else:
            for word in line.split():
                words.append(word)
            
with open("words.txt", "w") as f:
    for i in words:
        if (i in x and len(i) >= 3) or (i in poetryWords):
            f.write(i)
            f.write(" ")
    
