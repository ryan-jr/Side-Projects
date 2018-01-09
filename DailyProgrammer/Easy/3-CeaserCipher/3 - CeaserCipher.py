"""
[2/11/2012] Challenge #3 [easy]

Welcome to cipher day!

write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!
"""

import string
x = list(string.ascii_lowercase)
offset = 13


s = "hello world"
s = s.replace(" ", "")

for character in s:
  y = x.index(character)
  if y + offset > 26:
    y = (y + offset) % 13
    print(x[y])
  else:
    print(x[y + offset])



