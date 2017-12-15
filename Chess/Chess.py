# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:28:37 2017

@author: rjr
"""

# TODO: THE BOARD
# Every board has squares(64)
# Have the board draw 64 squares 
# Those squares need to be labeled from left to right A - H 
# and bottom to Top 1 - 8
# Each of the squares needs to contain the piece it (may) hold and its notation


  

def row():
    print("*" * 20) 
    

def vert1(data="  "):
    print("*", data, end="", sep="")
    

def vert2( data2="   "):
    
    print(data2, "*", end="")
    
    
           
            
def square2(data="  "):
    row()
    
    for i in range(0, 4):
        vert1("C1")
    print()
    print("*", end="")
    for i in range(0, 4):
        vert2("N")
    print()    
    
    
        
"""
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
for i in range(0, 8):
    square2()
    
row()


    