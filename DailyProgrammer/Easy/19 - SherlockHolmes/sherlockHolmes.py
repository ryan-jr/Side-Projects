# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:41:13 2018

@author: rjr


Challenge #19 will use The Adventures of Sherlock Holmes from Project Gutenberg.

Write a program that counts the number of alphanumeric characters there are in The Adventures of Sherlock Holmes. Exclude the Project Gutenberg header and footer, book title, story titles, and chapters. Post your code and the alphanumeric character count.

https://www.reddit.com/r/dailyprogrammer/comments/qlwrc/372012_challenge_19_easy/

Challenges:
    1.  How to add everything up from a set of readlines
    2.  Not using file.seek in order to skip past certain lines 
    3.  Figuring out where/how to start/stop
    4.  Not knowing the correct output (I'm assuming I'm correct)
        judging by the ranges that others are posting (432,139 to 431,301)
"""

excludeList = ["I. A Scandal in Bohemia", "II. The Red-headed League", "III. A Case of Identity",
    "IV. The Boscombe Valley Mystery", "V. The Five Orange Pips", "VI. The Man with the Twisted Lip",
    "VII. The Adventure of the Blue Carbuncle", "VIII. The Adventure of the Speckled Band", 
    "IX. The Adventure of the Engineer's Thumb", "X. The Adventure of the Noble Bachelor",
    "XI. The Adventure of the Beryl Coronet", "XII. The Adventure of the Copper Beeches", "ADVENTURE", "Title: The Adventures of Sherlock Holmes"]

lookup = "*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
lookup2 = "*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***"
y = 0
ctr = 0
linesList = []
otherCtr = 0

with open("SherlockHolmes.txt", "r") as f:
        x = f.readlines()
        for line in x:
            line = line.strip()
            if line in excludeList:
                print("Passing")
                pass
            else:
                linesList.append(line)
        
        
        linesList = linesList[45:12680]
        for j in linesList:
            for k in j:
                if k.isalpha() or k.isalnum():
                    otherCtr += 1

                
print(ctr)
print()
print(otherCtr)
                

   
    
    
    
    
    
"""

# Counters for lines that I want to exclude from the char count
for i in z:
            y += 1
            if i == "*":
                print("Character number:", y)
                
        z = list(str(x))
        z = z[669:627384]
        z = list(map(lambda s: s.strip(), z))
        for i in z:
            if i.isalpha() or i.isalnum():
                ctr += 1

             
"""