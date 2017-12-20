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
    
    print(len(data))
    return data
    
    
    
 

"""

Begin main program here

"""

# So many variables to initalize!
container = []
allocDict = {"A":0, "B":0, "C":0}
maxDict = {"A":0, "B":0, "C":0}
availDict = {"A":0, "B":0, "C":0}
procDict = {"Initalize":[], "P0":[], "P1":[], 
            "P2":[], "P3":[], "P4":[]}
initalCtr = 1

# Open the data from the original file
with open("344-BA.txt", "r") as f:
    while True:
        line = f.readline()
        container.append(filereader(line))
        if not line:
            break
        

# Flattening the list out so that we can add it to the 
# procDict correctly
temp = []
for data in container:
    temp += data
container = temp
print(container)

# Mapping the keys/values to the correct proccess
for k, v in procDict.items():
    print(k)
    if k is "Initalize":
        procDict[k] = container[0:3]
        del container[0:3]
    else:
        procDict[k] = container[0:6]
        del container[0:6]
        
temp = procDict["Initalize"]
availDict["A"] = temp[0]
availDict["B"] = temp[1]
availDict["C"] = temp[2]
print(availDict)



