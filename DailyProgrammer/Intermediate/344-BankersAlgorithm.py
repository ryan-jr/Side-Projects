# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:53:42 2017

@author: rjr
"""

def filereader(sequence):
    """Read a line from a file, determine what to do and return it.
    
        From a file read a line, figure if it is an initial
        allocation of memory, assign it properly and return that
        value.  If it is something to be processed return that 
        sequence correctly into the program.  
        
    Args:
        sequence: A sequence of characters read from a text file.
        
    Returns:
        Returns an array of characters(stripped of the first and
        last) to be proccess by other parts of the program.  
    
    Raises:
        N/A    
    """
    
    data = []
    
    
    for i in sequence:
        data.append(i)
    print(data)

    data = data[1:-1]
    print(data)
    data = data[0::2]

    data = [int(x) for x in data]
    print(data)
    
    
    return data
    
    
    
container = []  
  
with open("344-BA.txt", "r") as f:
    while True:
        line = f.readline()
        container.append(filereader(line))
        if not line:
            print("Hello")
            break
        

print(container)

