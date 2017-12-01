# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:11:30 2017

@author: rjr
"""
# Import regex
import re

def packetCompare(packetList):
    finalList = []
    print(packetList)
    # TODO: Loop through the 2d list and compare the neccessary parts
    # From there put them in the list 
    # What if the pNum doesn't match, where does it go?
    # What if the pNum is greater than or less than, where does it go?
    # Could we just use a dict with [i][j] with i being used as the 
    # key, and if the key is in the DS then just append i and go from 
    # there?
    # How do I arrange the sequence though?
    # Could I create K/V pairs based on the seq number?


def packetArr(pNum, seq, tot, data):
    pNum = int(pNum)
    seq = int(seq)
    tot = int(tot)
    dataList = []
    dataList.append([pNum, seq, tot, data])
    # print(dataList[0][3])
    packetCompare(dataList)

 # Opens the file and then loops through it, splitting the packet
# number into it's own string. 

data = open("DailyProg333Easy.txt", "r")


# Here we do a regex search for what we want
for info in data:
    regex = re.compile(r'([0-9]{4})\s*(\d*)\s*(\d*)\s*(.*)')
    match = regex.search(info)
    
    packetArr(match.group(1), match.group(2), match.group(3), match.group(4))
    
    
    

