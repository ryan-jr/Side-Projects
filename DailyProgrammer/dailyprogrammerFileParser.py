# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:43:23 2017

@author: rjr
"""


def redditTable(date, idNum, difficulty, title, url):
    
    
    print(date, "|", idNum, "|", difficulty, "|", title, "|", "[post]", "(", url, ")")
    


# Script to parse r/dailyprogrammer output
f = open("dailyprogrammerOutput2.txt", "r")

lineList = f.readlines()
    
# Creating the list of post titles
postTitleList = lineList[::8]


# Getting the indexes that match the given string, and then appending them
indexes = []
urlList = []
masterList = []
dateList = []
idList = []
difficultyList = []
titleList = []

for i, element in enumerate(lineList):
    if "https://www.reddit.com/r/dailyprogrammer" in element:
        indexes.append(i)
        
for i in indexes:
    urlList.append(lineList[i][:-1])
  

# Reversing everything to make it easier to iterate over later
#urlList = list(reversed(urlList))
#postTitleList = list(reversed(postTitleList))

for i in range(len(urlList)):
    print(postTitleList[i], urlList[i])



# Zipping the lists together to better associate them
# before breaking them into their constituent parts and stuffing them in a table
comboList = (list(zip(postTitleList, urlList)))


# Looping through the combined list and grabbing different parts to separate out
# in order to manipulate them more easily at the end
for i in range(0, len(comboList)):
    dateList.append(comboList[i][0][1:11])
    

for i in range(0, len(comboList)):
    idList.append(comboList[i][0][24:27])


for i in range(0, len(comboList)):
    try:
        if "[E" in comboList[i][0]:
            difficultyList.append("Easy")     
        elif "[I" in comboList[i][0]:
            difficultyList.append("Intermediate")
        elif "[H" in comboList[i][0]:
            difficultyList.append("Hard")
    except:
        pass

for i in range(0, len(comboList)):
    titleList.append(comboList[i][0][34:-1])
    


finalList = (list(zip(dateList, idList, difficultyList, titleList, urlList)))

print(finalList)

print("Date | ID | Difficulty | title | link")
print("---------|----------|----------|----------|----------")
for i in finalList:
    redditTable(i[0], i[1], i[2], i[3], i[4])
    
hardList = []
easyList = []
InterList = []


for i in finalList:
    if i[2] == "Hard":
        hardList.append(i[3])
        hardList.append(i[4])
        
for i in hardList:
    print(i)



