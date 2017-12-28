"""
[easy] challenge #2


Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

"""

# Year long savings calculator

def day(amount):
  """Function to calculate the daily amount needed in order to achieve a savings goal 
  for a given year 
  
     Takes in one arg (amount) which is a float and calculates the daily savings needed 
     to achieve the amount that the person wants to save
     
     Arguments:
            Amount: A positive float that is the savings goal 
      
     Returns: 
            Returns a float that is the amount divided by 365
            
     Raises:
            N/A
  
  """
  if amount >= 365:
    return ("{0:.2f} dollar(s)".format(round(amount/365,2)))
  else:
    return ("{0:.2f} cents".format(round(amount/365,2)))

def week(amount):
  """Function to calculate the weekly amount needed in order to achieve a savings goal 
  for a given year 
  
     Takes in one arg (amount) which is a float and calculates the weekly savings needed 
     to achieve the amount that the person wants to save
     
     Arguments:
            Amount: A positive float that is the savings goal 
      
     Returns: 
            Returns a float that is the amount divided by 52
            
     Raises:
            N/A
  
  """
  
  if amount >= 365:
    return ("{0:.2f} dollar(s)".format(round(amount / 52, 2)))
  else:
    return ("{0:.2f} cents".format(round(amount / 52, 2)))

def month(amount):
  """Function to calculate the monthly amount needed in order to achieve a savings goal 
  for a given year 
  
     Takes in one arg (amount) which is a float and calculates the monthly savings needed 
     to achieve the amount that the person wants to save
     
     Arguments:
            Amount: A positive float that is the savings goal 
      
     Returns: 
            Returns a float that is the amount divided by 12
            
     Raises:
            N/A
  
  """
  
  if amount >= 365:
    return ("{0:.2f} dollar(s)".format(round(amount / 12, 2)))
  else:
    return ("{0:.2f} cents".format(round(amount / 12, 2)))



amount = input("How much would you like to save this year?: ")
try:
  amount = float(amount)
  if amount <= 0:
    print("A zero/negative number is not valid!")
    exit()
except:
  print("Please enter a valid number/input")
  exit()
  
print("Ok, you want to save: ", amount, 
" this year.  This can be done by saving (roughly) ", day(amount)," a day",  week(amount),"dollars a week",  month(amount),"dollars a month")
  
  
