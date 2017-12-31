# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:43:23 2017

@author: rjr
"""

# Script to parse r/dailyprogrammer output

f = open("dailyprogrammerOutput2.txt", "r")

lineList = f.readlines()
    
# Creating the list of post titles
postTitleList = lineList[::8]

# Getting the indexes that match the given string, and then appending them
indexes = []
urlList = []
for i, element in enumerate(lineList):
    if "https://www.reddit.com/r/dailyprogrammer" in element:
        indexes.append(i)
        

for i in indexes:
    urlList.append(lineList[i])
    



# Zipping the lists together to better associate them
# before breaking them into their constituent parts and stuffing them in a table
x = (zip(postTitleList, urlList))
print(x)







