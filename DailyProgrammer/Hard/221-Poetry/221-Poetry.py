# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:14:25 2018

@author: rjr
"""
import datetime


# Iterate over the lines of the file checking each of the words and seeing 
# if they contain the most common words in the dictionary, if they do, add that line 
# to a list

print(datetime.datetime.now())

with open("belowSeventy.txt", "r") as f:
    x = f.readlines()
    
ctr = 0  
x = list(map(lambda s: s.strip(), x))

with open("poetry.txt", "r") as f:
    for line in f:
        ctr = 0
        print("Parsing line!", datetime.datetime.now())
        for word in line.split():
            if len(word) >= 15 or len(word) <= 2:
                pass
            else:
                with open("sentences2.txt", "a") as g:
                    if word in x:
                        ctr += 1
                        if ctr >= 4:
                            print(ctr)
                            print("Output to console!", datetime.datetime.now())
                            g.write(line)
                            break
                                
                                
                                        
    
print(datetime.datetime.now())
"""
# appending the line if if one of the words from poetry matches 
                if word in poetryWords:
                    lines.append(line)
                    
# Trying to add/find words that are the average length in english:
    # (i in x and len(i) >= 3) or 
    
    words.append(word)
    
    for word in line.split():
with open("sentences.txt", "w") as f:
    for i in words:
        if i in x:
            f.write(i)
            f.write(" ")
    

print(len(words))
print(words)

with open("allthewords.txt", "a") as h:
    for i in words:
        h.write(" ")
        h.write(i)
    
"""