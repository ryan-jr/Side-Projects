"""
[2/16/2012] Challenge #8 [easy]

write a program that will print the song "99 bottles of beer on the wall".

for extra credit, do not allow the program to print each loop on a new line.


https://www.reddit.com/r/dailyprogrammer/comments/pserp/2162012_challenge_8_easy/
"""



for i in range(100, 0, -1):
  
  if i == 1:
    print(i, "bottle of beer on the wall", i, "bottle of beer ", end="")
    print("take one down, pass it around, no more beer on the wall")
  else:
    print(i, "bottles of beer on the wall", i, "bottles of beer ", end="")
    print("take one down pass it around", i - 1, "bottles of beer on the wall")
    
