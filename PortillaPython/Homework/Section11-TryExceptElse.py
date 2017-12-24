# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 10:40:25 2017

@author: rjr


# Problem 1
for i in ["a"]:
    try:
        print(i ** 2)
    except:
        TypeError
        print("Not a valid input")
        
        
# Probelm 2
x, y = 5, 0



try:
    z = x / y
      
except:
    ZeroDivisionError
    print("Divivision by Zero")
    print("x:", x, "divided by y:", y, "is invalid") 
finally:
    print("Operation Completed")
"""

# Problem 3
def ask():
    x = True
    while x:
        try:
            y = input("Please input a number to square: ")
            print(int(y) ** 2)
        except:
            TypeError
            print("invalid operation please try again...")
        else:
            x = False
            

ask()
        



