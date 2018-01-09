# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:35:34 2018

@author: rjr
"""

import random


def pwdFunc(lines, asciiList):
    
    pwdList = []
    
    for i in range(0, 2):
        x = random.choice(lines)
        pwdList.append(x.capitalize())
        y = random.choice(asciiList)
        pwdList.append(chr(y))
        if i == 1:
            pwdList.append(str(random.randint(0, 99)))
            
    return "".join(pwdList)
    
pwdList = []
asciiList = [33, 35, 36, 37, 38, 42, 43, 45, 63, 61]
lines = open("10kWords.txt").read().splitlines()

for i in range(0, 10):    
    print(pwdFunc(lines, asciiList))



