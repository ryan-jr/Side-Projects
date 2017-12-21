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

    # Cutting the first and last values because they are junk strings
    # Striding every other item to get rid of spaces
    # Finally turning everything into an integer rather than a string
    data = data[1:-1]
    data = data[0::2]
    data = [int(x) for x in data]
    
    return data
    
 
def compareAvailToMax(availDict, maxArr, allocArr):
    """Check and see if the resources available are able to meet the needs 
       of the maximum required resources.
    
       Takes in the available resources, maximum resources, and allocated
       resources.  Checks to see if the inital index of the max resources
       is a signal value, if not, then runs the neccessary comparisons.  
        
    Args:
        availDict: Dictionary of available resources
        maxArr: List of maximum resoures required
        allocArr:List of allocated resources
        
    Returns:
        Returns True or False based on the available resources meeting 
        the needs of the proccess or not.  
    
    Raises:
        N/A    
    """
    if maxArr[0] == 9999:
        return False
    
    x = availDict["A"] + allocArr[0]
    y = availDict["B"] + allocArr[1]
    z = availDict["C"] + allocArr[2]
    

    if availDict["A"] >= maxArr[0] and  availDict["B"] >= maxArr[1] and availDict["C"] >= maxArr[2]:
        return True
    elif x >= maxArr[0] and y  >=  maxArr[1] and z >=  maxArr[2]:
        return True
    else: 
        return False

def addAllocToAvail(avail, allocArr):
    """This funcion only runs if a proccess has completed and is freeing
       up resources to the available dictionary.  
    
       Add the correct values from the allocated resources to the available
       dictionary.  
        
    Args:
        avail: The available dictionary with initial/starting values
        allocArr: The list of allocated resources for the process.  
        
    Returns:
        Returns the modified/updated available dictionary.  
    
    Raises:
        N/A 
    """
    avail["A"] += allocArr[0]
    avail["B"] += allocArr[1]
    avail["C"] += allocArr[2]
    
    return avail
    
def poppingOff(procDict, k, procLen):
    """OK, you can't actually pop things off of a dictionary while looping
    through it, because otherwise you throw a RuntimeError, so my thrown
    together solution is to replace the dict value with something that
    wouldn't run (in almost all probabilities)
    
        
    Args:
        procDict: The proccess dictionary that has the resources mapped to
        the values they contain.  
        k: The key from procDict
        procLen: The length of procdict(used to update the loop that the 
        variable is returned to)
        
    Returns:
        procDict: procDict with updated values.
        procLen: Used as a comparision value to determine if the loop should
                 continue.  
    
    Raises:
        N/A 
    
    """
    
    procDict[k] = [9999, 9999, 9999, 9999, 9999, 9999]
    procLen -= 1
    return procDict, procLen








# __main()__
container = []
availDict = {"A":0, "B":0, "C":0}
procDict = {"Initalize":[], "P0":[], "P1":[], 
            "P2":[], "P3":[], "P4":[]}
initalCtr = 1


# Read in data
with open("344-BA.txt", "r") as f:
    while True:
        line = f.readline()
        container.append(filereader(line))
        if not line:
            break
        
# Flattening the list out so that we can add it to procDict
temp = []
for data in container:
    temp += data
container = temp

# Mapping the keys/values to the correct proccess
# Deleting the arrays after we are done with them
for k, v in procDict.items():
    if k is "Initalize":
        procDict[k] = container[0:3]
        del container[0:3]
    else:
        procDict[k] = container[0:6]
        del container[0:6]

# Mapping k/v to prime our process list     
temp = procDict["Initalize"]
availDict["A"] = temp[0]
availDict["B"] = temp[1]
availDict["C"] = temp[2]

# Removing intialize from the Proccess dictionary (We don't need it anymore)
procDict.pop("Initalize", 0)


# Intializing variables for the loop
procLen = len(procDict)
procExecutionOrder = []

"""
The following code: 

Loops through the dict while there are still valid values
grabs maxArr/allocArr from the front/back of the list respectively
to use to compare/add to available arr
When true we add alloc to available, preserve the order we executed steps in, and update the process dict and how many valid values are left
"""
while procLen > 0:
    for k, v in procDict.items():
        maxArr = procDict[k][3:]
        allocArr = procDict[k][0:3]
        x = compareAvailToMax(availDict, maxArr, allocArr)
        if x == True:
            availDict = addAllocToAvail(availDict, allocArr)
            procExecutionOrder.append(k)
            procDict, procLen = poppingOff(procDict, k, procLen)
 
print(procExecutionOrder)

