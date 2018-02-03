"""
CTCI 1.1
Implement an algorithm to determine if a string has all unique characters.

What if you cannot use additional data structures
"""

# Part 1
# The idea here is to store all unique characters 
# in a dictionary and if there is a repeat to break

dictionary = {}
string = "dig xcn"

for i in string:
  print(i)
  if i in dictionary:
    dictionary[i] += 1
    print("Not unique!")
    break
  else:
    dictionary[i] = 1

# If I couldn't use additonal data structures I would likely use find/index or something similar 
# But I honestly don't know if using what's built into a string is "An additional data structure"
for i, item in enumerate(string):
  searchTerm = string[i]
  searchSpace = string[i + 1:-1]
  
  if searchSpace.find(searchTerm) != -1:
    print("not unique!")
    break

# Loop through the characters (twice), if more than one instance of the character(s) is/are found, break
for char in string:
  foundCounter = 0 
  for char2 in string:
    if char == char2:
      foundCounter += 1
      
    if foundCounter > 1:
       print("not unique!")
       break
  
# Another way to solve it:
# Found via https://stackoverflow.com/questions/17357370/implementing-an-algorithm-to-determine-if-a-string-has-all-unique-characters
x = len(set(string))
y = len(string)
print(x == y)

"""
More pythonic answer:

def unique(s):
    return len(set(s)) == len(s)
    
# Note: You can't simply print the above because it will return an error of "Type bool does not have method len"
# Because at that point Python is trying to determine the length of True or False

"""