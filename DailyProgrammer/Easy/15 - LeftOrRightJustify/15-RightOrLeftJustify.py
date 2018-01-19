# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 18:34:06 2018

@author: rjr
"""

"""

Write a program to left or right justify a text file

https://www.reddit.com/r/dailyprogrammer/comments/q4c34/2242012_challenge_15_easy/
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x))

"""
def userFileJustify(justify, filename):
  length = 200
  length2 = 0
  userWrite = input("What do you want to write to the file: ")
  with open(filename, "a") as f:
      
    if justify == "1":
        f.write(userWrite.rjust(length))
    else:
        f.write("\n")
        f.write(userWrite.ljust(length2))



length = 200
length2 = 0

userAction = input("Would you like to \n1.  write to a file OR \n2.  write the information to the console.")

if userAction == "1":
  print("Ok, please put in the filename:")
  print("NOTE: Include the file extension (.txt , .pdf , etc...")
  userFile = input(">")
  userFile = f'{userFile}'
  justifyChoice = input("1.  Right Justify \n2.  Left Justify")
  userFileJustify(justifyChoice, userFile)
else:
  justifyChoice = input("1.  Right Justify \n2.  Left Justify")
  userText = input("Waiting for text input: ")
  if justifyChoice == "1":
      print(userText.rjust(25))
  else:
      print("\n")
      print(userText.ljust(length2)) 