"""
https://www.reddit.com/r/dailyprogrammer/comments/q2v2k/2232012_challenge_14_easy/


Input: list of elements and a block size k or some other variable of your choice

Output: return the list of elements with every block of k elements reversed, starting from the beginning of the list.

For instance, given the list 12, 24, 32, 44, 55, 66 and the block size 2, the result is 24, 12, 44, 32, 66, 55.

"""

def listSwitch(userList, blockSize):
  """
  
  """
  ctr = 0
  newList = []
  print(userList)
  temp = 0
  
  # Grab from start to end of blocksize 
  # Reverse that block 
  # Put that into a new list 
  
  for i in userList:
    if temp + blockSize == len(userList):
      x = userList[temp:temp + blockSize]
      newList.append(list(reversed(x)))
      break
    elif ctr == 0:
      temp = ctr
      x = userList[temp:temp + blockSize]
      newList.append(list(reversed(x)))
      ctr += 1
    else:
      temp = ctr
      x = userList[temp:temp + blockSize]
      newList.append(list(reversed(x)))
      ctr += 1

  print(newList)


data = [12, 24, 32, 44, 55, 66]
listSwitch(data, 2)
