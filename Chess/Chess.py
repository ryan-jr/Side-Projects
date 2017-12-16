# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:28:37 2017

@author: rjr
"""
from string import ascii_lowercase


# TODO: THE BOARD
# Every board has squares(64) (done)
# Have the board draw 64 squares  (done)
# Those squares need to be labeled from left to right A - H 
# and bottom to Top 1 - 8
# Each of the squares needs to contain the piece it (may) hold and its notation


def row():
    print("-" * 25) 
    

def vert1(data="  "):
    print("|", data, end="", sep="")
    

def vert2( data2="   "):
    
    print(data2, "|", end="")
    
    
def square2(data="  "):
    
    z = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 
'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 
'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 
'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 
'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 
'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 
'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']  
    row()
    
    for i in range(0, 8):
        vert1(z[i * data])
    print("|")
    print("|", end="")
    for i in range(0, 8):
        vert2("N")
    print()    
    






"""

for letter in range(65, 73):
    for i in range(1, 9):
        #print(chr(letter),end="")
        #i = str(i)
        x = chr(letter) + str(i)
        z.append(x)
        
  
print(z)
for i in range(0, 17):
    if i % 8 == 0:
        print()
    else:
        square()
        
        

def square():                                                    
    for i in range(0, 4):
        if i == 0:
            print("*" * 5)
        elif i == 3:
            print("*" * 5)
        else:
            print("*" + "   " + "*")
"""

"""
for chessRow in range(1, 9):
    for col in range(1, 9):
        square2(chessRow * col)
 """
for i in range(1, 9):
    square2(i)
    
row()


    