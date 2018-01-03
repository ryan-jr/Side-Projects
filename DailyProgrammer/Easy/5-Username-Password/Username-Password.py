# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 18:57:01 2018

@author: rjr
"""

"""

# Username/Password

https://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/

Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file.

for even more extra credit, break into your own program :)

"""

userPass = []
guess = False

with open("passwordFile.txt") as file:
    userPass = file.readlines()
    userPass = list(map(lambda i: i.strip(),  userPass))

print(userPass)
while guess == False:
    user = input("Please input your username: ")
    pwd = input("Please input your password: ")
    if user == userPass[0] and pwd == userPass[1]:
        guess = True
        print("welcome!")

        

