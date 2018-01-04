from decimal import *

def plouffBig(n):
    """A function to calculate pi to (n) percision using the Plouffe formula
  
  
    Args:
      n: An intial value to determine how many loops to run/to a level of percision
    
    Returns:
      Returns pi
    
    Raises:
      N/A 
      
      
      https://www.reddit.com/r/dailyprogrammer/comments/pp53w/2142012_challenge_6_easy/?st=jbzrt6kb&sh=9eb2234b
    """
    # http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    # Decimal is useful: https://docs.python.org/2/library/decimal.html#decimal.getcontext
    
    pi = Decimal(0)
    getcontext().prec = 35 # Setting precision level for the decimal
    k = 0
    
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
        
    return pi
    
    
print(plouffBig(35))