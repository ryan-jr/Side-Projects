"""

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


https://webcache.googleusercontent.com/search?q=cache:aGkZ6kUo-bMJ:https://projecteuler.net/problem%3D8+&cd=2&hl=en&ct=clnk&gl=us

https://www.w3resource.com/python-exercises/python-basic-exercise-115.php

https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list

"""

def multipLoop(listData):
  tot = 1
  for i in listData:
    tot *= i 
    
  return tot

    

data = [8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1]


total = 0 
length = len(data)
ctr = 0

while ctr <= length - 4:
  tempTotal = multipLoop(data[ctr:ctr + 4])
  if tempTotal > total:
    total = tempTotal
  ctr += 1
  
print(total)
