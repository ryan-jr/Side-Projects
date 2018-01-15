"""
Anna.
Civic
Kayak
Level
Madam
Mom
Noon
Racecar
"""

def isPalindrome(word):
  """Function to check if a word is a palindrome 
  
  Args:
    word: A string 
    
  Returns:
    boolean: A boolean value that is true/false
    
  Raises:
    N/A
  """
  boolean = True
  
  forward = list(word.lower())
  print(forward)
  backward = "".join((reversed(word.lower())))
  print(backward)

  for count, letter in enumerate(forward):
    if letter == backward[count]:
      pass
    else:
      boolean = False
      break
      
  
  return boolean

print(isPalindrome("Racecar"))
