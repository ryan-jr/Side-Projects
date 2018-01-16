# Anagramp problem

# Given two strings, check to see if they are anagrams
def anagramCheck(str1, str2):
  str1 = list(str1.replace(" ", "").lower())
  str2 = list(str2.replace(" ", "").lower())

  x = sorted(str1)
  y = sorted(str2)
  
  if len(str1) != len(str2):
    return False
  
  for count, i in enumerate(x):
    if i != y[count]:
      return False
      
      
  return True
  
  

"""

Note: The above can also be acomplished as such:


def anagramCheck(str1, str2):
  count = {}
  
  for letter in str1:
    if letter in count:
      count[letter] += 1 
    else:
      count[letter] = 1 
      
  for letter in str2:
    if letter in count:
      count[letter] -= 1 
    else: 
      count[letter] = 1 
      
  for k, v in count.items():
    if v != 0:
      return False 
      
  return True 
"""

print(anagramCheck("public relations", "crap built on lies"))