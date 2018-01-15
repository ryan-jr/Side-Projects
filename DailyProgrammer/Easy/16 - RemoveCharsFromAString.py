"""
Write a function that takes two strings and removes from the first string any character that appears in the second string. For instance, 
if the first string is “Daily Programmer” and the second string is “aeiou ” the result is “DlyPrgrmmr”.
note: the second string has [space] so the space between "Daily Programmer" is removed

https://www.reddit.com/r/dailyprogrammer/comments/q8aom/2272012_challenge_16_easy/
"""

# Initializing variables
initialString = "Daily Programmer"
correctString = ""
extractString = "aeiou "
extractList = []

# .split() removes the " " from the extractString
for i in extractString:
  extractList.append(i)
 
# Going through the string, comparing, and adding to the correctString based on the outcome
for c in initialString:
  if c in extractList:
    correctString += "" 
  else:
    correctString += c 
    
print(correctString)
