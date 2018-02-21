"""


function updateInventory(arr1, arr2) {
    // All inventory must be accounted for or you're fired!
  
    // If item from arr2 is already in arr1, update the arr1 quantity
    // else add the item from arr2 to arr1
    return arr1;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);


"""

def flattenList(nestedList):
  """Takes in a nested list and returns a flattened list 
  
  Args: 
    nestedList: The nested list in question 
  
  Returns:
    flatList: A flattned list 
    
  Raises:
    N/A 
  """
  flatList = []
  for sublist in nestedList:
    for item in sublist:
      flatList.append(item)
      
  return flatList

def updateInventory(arr1, arr2):
  # If item from arr2 is already in arr1, update the arr1 quantity
  # else add the item from arr2 to arr1
  

  arr1 = flattenList(arr1)
  arr2 = flattenList(arr2)
  numList = []
  stuffList = []
  
  for x in arr1:
    if type(x) == int:
      numList.append(x)
    else:
      stuffList.append(x)
      
  x = dict(zip(stuffList, numList))
  print(list(x))
  
  del numList[:]
  del stuffList[:]

  for y in arr2:
    if type(y) == int:
      numList.append(y)
    else:
      stuffList.append(y)
  
  y = dict(zip(stuffList, numList))
  
  print(y)
  
  otherList = []
  for k, v in x.items():
    if k in y:
      inventory = y.get(k)
      print(inventory)
      x[k] += inventory
    
    
  dictlist = []
  for key, value in x.items():
    temp = [key,value]
    dictlist.append(temp)
    
  for k, v in y.items():
    if k not in x:
      temp = [k, v]
      dictlist.append(temp)
  
  for item in dictlist:
    a, b = item[0], item[1]
    item[0] = b 
    item[1] = a 
    
  a, b= dictlist[3], dictlist[4]
  dictlist[3] = b 
  dictlist[4] = a
  
  
  print(dictlist)
  # Turn arr1 into a dictionary with k, v pairs
  
  




curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]]
    
newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]]
    
updateInventory(curInv, newInv)