# Random Password Generator
# Taking a random sample this version with a password length of 8 characters scores ~73% on avg according to:
# http://www.passwordmeter.com/

import random

def passwordGenerator(noGo):
  """Generates a random password of 8 characters 
  
    Args: 
       Takes in a list of integers that correspond with ASCII characters that are not valid/bad
       
    Returns:
       A valid (currently 8 character) pwd
       
    Raises:
    
  
  
  
  
  Note:
      Taking a random sample this version with a password length of 8 characters scores ~73% on avg according to: http://www.passwordmeter.com/
  """
  
  pwd = []
  while len(pwd) < 8:
    x = random.randrange(33, 123)
    
    if x in noGo:
      pass
    else:
      pwd.append(chr(x))
      
    
  return "".join(pwd)


noGoList = [95, 39, 60, 92, 59, 32, 34, 91, 93, 94, 96, 40, 41, 43, 44, 46, 47, 58, 62]

for i in range(0, 11):    
  print(passwordGenerator(noGoList))


avgList = [86, 66, 94, 56, 60, 68, 58, 87, 72, 72, 82]

sum = 0 


for i in avgList:
  sum += i 
  
print(sum/len(avgList))
