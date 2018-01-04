# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:29:41 2018

@author: rjr
"""

"""
[2/15/2012] Challenge #7 [easy]
submitted 5 years ago by bholzer0 0[M]

Write a program that can translate Morse code in the format of ...---...

A space and a slash will be placed between words. ..- / --.-

For bonus, add the capability of going from a string to Morse code.

Super-bonus if your program can flash or beep the Morse.

This is your Morse to translate:

.... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--


https://www.reddit.com/r/dailyprogrammer/comments/pr2xr/2152012_challenge_7_easy/?st=jc00cjzv&sh=aaab66b4

"""
def flattenList(nestedList):
  """Takes in a nested list and returns a flattened list 
  
  Args: 
    nestedList: The nested list in question 
  
  Returns:
    flatList: A flattned list 
    
  Raises:
    N/A 
  """
  flatList = []
  for sublist in nestedList:
    for item in sublist:
      flatList.append(item)
      
  return flatList

# Our starting string
morseString = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"

# Declaring neccessary lists to work with
morseList = morseString.split(" /")
morseLetters = []


for x in morseList:
  morseLetters.append(x.split(" "))
  
  
morseFlatList = []

for sublist in morseLetters:
    for item in sublist:
        morseFlatList.append(item)

# Getting a morse code list from a file that was found online
with open("morseCode.txt") as f:
  lines = f.read().splitlines()
  
# Creating the list from the file
translateList = []
for i in lines:
    translateList.append(i.split(" "))
translateList = flattenList(translateList)

# Stripping all tabs out of the file and putting it into a dict
strippedTranslateList = []
for stuff in translateList:
    strippedTranslateList.append(stuff.split("\t"))
    
strippedTranslateList = flattenList(strippedTranslateList)


translateDict = dict(zip(strippedTranslateList[0::2], strippedTranslateList[1::2]))
print(translateDict)
    

print(morseFlatList)
for i in morseFlatList:
    print(i)
    

listValues = []
for i in morseFlatList:
   print(list(key for key, value in translateDict.items() if value == i))
    
print(listValues)
        

"""

Full-stop (period)	.-.-.-
Comma	--..--
Colon	---...
Question mark (query)	..--..
Apostrophe	.----.
Hyphen	-....-
Slash ("/")	-..-.
Brackets (parentheses)	-.--.-
Quotation marks	.-..-.
At sign	.--.-.
Equals sign	-...-



"""
