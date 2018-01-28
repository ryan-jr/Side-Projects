"""

create a program that will find all prime numbers below 2000

# Verified as correct as per: https://www.miniwebtool.com/list-of-prime-numbers/?to=2000

https://www.reddit.com/r/dailyprogrammer/comments/qnkro/382012_challenge_20_easy/
"""

import math

def primeCheck(size):
  """Returns a list of prime numbers using the sieve of Eratosthenes
  
  """
  # Intializing the sieve
  sieve = [True] * size
  sieve[0] = False
  sieve[1] = False
  
  for i in range(2, int(math.sqrt(size)) + 1):
    pointer = i * 2 
    while pointer < size:
      sieve[pointer] = False
      pointer += i
      
  primes = []
  for i in range(size):
    if sieve[i] == True:
      primes.append(i)
  print(len(primes))
  return primes
  
x = primeCheck(2000)
print(x)
