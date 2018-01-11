"""
https://www.reddit.com/r/dailyprogrammer/comments/pzo4w/2212012_challenge_13_easy/

Find the number of the year for the given date. For example, january 1st would be 1, and december 31st is 365.

for extra credit, allow it to calculate leap years, as well.

"""

def leapCheck(n):
  """A function to check if a year is a leap year 
  
  Args:
    n: A year provided as an integer
    
  Returns:
    True/False: Returns a boolean, True if a year is a leap year, False otherwise
    
  Raises:
    N/A
  
  
  """
  
  if n % 400:
    return True
  elif n % 100:
    return False
  elif n % 4:
    return True
  


# Opting to use list due to being able to manipulate them by numeric indicies
monthList = [ "Jan", 31, 
              "Feb", 28,
              "Mar", 31,
              "Apr", 30,
              "May", 31,
              "Jun", 30,
              "Jul", 31,
              "Aug", 31,
              "Sep", 30,
              "Oct", 31,
              "Nov", 30,
              "Dec", 31 ]
              
print("A program to determine what day of the year it is")
userInput = input("Please input the month and day(e.g. Jan, 1, 2020)")


userMonth, userDay, userYear = userInput.split(",")
userDay = int(userDay)
userYear = int(userYear)
userYear = leapCheck(userYear)
listIndex = monthList.index(userMonth)


if listIndex == 0:
  print(userDay)
elif userYear == False:
  x = monthList[1:listIndex:2]
  print(sum(x) + (monthList[listIndex + 1]) - (monthList[listIndex + 1] - userDay))
else:
  x = monthList[1:listIndex:2]
  print(sum(x) + (monthList[listIndex + 1]) - (monthList[listIndex + 1] - userDay) + 1)
