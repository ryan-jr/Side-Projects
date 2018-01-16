"""
A Pythagorean triplet is a set of three natural numbers, a b c, for which,

a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.


https://webcache.googleusercontent.com/search?q=cache:P5MdRjeADaAJ:https://projecteuler.net/problem%3D9+&cd=1&hl=en&ct=clnk&gl=us
https://stackoverflow.com/questions/2769842/project-euler-9-understanding
"""
import math




for i in range(0, 20):
  a = i ** 2 
  print("A:", a)
  b = (i + 1) ** 2 
  print("B:", b)
  c = a + b 
  print("C:", c)
  
  x = math.sqrt(a) + math.sqrt(b) + math.sqrt(c)
  print(x)
  
  
