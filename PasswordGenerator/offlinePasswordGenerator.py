import random


def pwdFunc(asciiList, excludeList):
    """A function to create a password 10 characters long with random characters 
    
    Args:
      asciiList: A list of ASCII approved characters (in integer format)
      excludeList: A list of ASCII characters that should not be in a password 
      
    Returns:
      pwdList: A list of 10 passwords 10 charaters long 
      
    Raises:
      N/A
    
    """
    pwdList = []
    
    for i in range(0, 10):
        y = random.randint(48, 122)
        if y in excludeList:
          y = random.choice(asciiList)
          pwdList.append(chr(y))
        else:
          pwdList.append(chr(y))
            
    return "".join(pwdList)
    
pwdList = []
excludeList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 40, 41, 46, 123, 124, 125, 126, 127, 58, 59, 60, 61, 62, 63, 90, 91, 92, 93, 94, 95, 96]
asciiList = [33, 35, 36, 37, 38, 42, 43, 45, 63, 61]

for i in range(0, 10):    
    print(pwdFunc(asciiList, excludeList))
    
