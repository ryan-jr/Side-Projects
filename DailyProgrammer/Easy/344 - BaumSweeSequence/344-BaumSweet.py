# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:39:13 2017

@author: rjr
"""

import math

def baumSweet(number):
  """Docstring here 
  
  """
  print(number)
  print("Hello")
  # Base case
  if number == 0:
    return 1
    
  elif number % 4 == 0:
    
    print((number - 1) / 2)
    x =((number - 1) / 2)
    print(baumSweet(math.ceil(((number - 1) / 2))))
  
    
  elif number % 2 == 0:
   return 0
    
  


print(baumSweet(76))
