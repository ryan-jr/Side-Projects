"""
A Pythagorean triplet is a set of three natural numbers, a b c, for which,

a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.


https://webcache.googleusercontent.com/search?q=cache:P5MdRjeADaAJ:https://projecteuler.net/problem%3D9+&cd=1&hl=en&ct=clnk&gl=us
https://stackoverflow.com/questions/2769842/project-euler-9-understanding

http://www.friesian.com/pythag.htm
"""
import math




for i in range(0, 10):
  a = i ** 2 
  a2 = i 
  print("A:", a)
  b = (i + 1) ** 2 
  b2 = (i + 1) 
  print("B:", b)
  c = a + b 
  x = a2 + b2 + math.sqrt(c)
  print("C2:", x)
  print("C:", c)
  
  x = math.sqrt(a) + math.sqrt(b) + math.sqrt(c)
  print(x)
  
  
