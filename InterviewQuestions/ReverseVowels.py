# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:11:00 2017

@author: rjr
"""

# Given a word reverse the vowels in that word
# ex: apple becomes eppla, friend becomes freind, etc...

def vowelReverse(word):
  """Reverses vowels in a given word
  
     This function takes in a given word as a string 
     and prints out the word with vowels reversed.  
     
     Args:
        Takes in a word as a string 
        
     Returns:
        N/A 
      
     Raises:
        N/A
  
  
  """
  l = []
  indexHolder = []
  letterHolder = []
  vList = ["a", "e", "i", "o", "u"]
  for i in word:
    l.append(i)
    if i in vList:
      print(l.index(i))
      indexHolder.append(l.index(i))
      letterHolder.append(l[l.index(i)])
    else:
      pass
    
  letterHolder = letterHolder[::-1]
  ctr = 0
  for i in indexHolder:
    l[i] = letterHolder[ctr]
    ctr += 1
  
  #print(l, indexHolder[::], letterHolder)
  print(l)

vowelReverse("friend")