# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:05:48 2018

@author: rjr
"""

"""
Write a small program that can take a string:
"hi!"
and print all the possible permutations of the string:
"hi!"
"ih!"
"!hi"
"h!i"
"i!h"
etc...
https://www.reddit.com/r/dailyprogrammer/comments/pxs2x/2202012_challenge_12_easy/

"""


def stringPermutations(lst):
  """Function to determine the permutations in a string
  
  This is a recursive based function that takes in the string as a list
  and returns all permutations that are possible.  
  
  Args:
      lst: The provided string as a list
  
  Returns:
      permutationList: A list that contains all of the characters from the 
      provided list
  
  Raises:
      N/A
  
  # NOTE: This function can also be acomplished with the one liner:
      # (Assuming we are accepting user input)
      # import itertools 
      # print([''.join(x) for x in itertools.permutations(input())])
      
  # But doing a one liner like this, defeats some purposes of the exercise


  """
  
  permutationList = []
  stringLength = len(lst)
  remList = []
  
  # Base case if nothing in the string/only one permutation possible
  if stringLength == 0 or stringLength == 1:
    return lst 
  else:
    for i in range(stringLength):
      j = lst[i]
      
      remList = lst[:i] + lst[i + 1:]
      
      for p in stringPermutations(remList):
          permutationList.append(j + p)
          
    return permutationList


data = list("hi!")
for p in stringPermutations(data):
    print(p)

