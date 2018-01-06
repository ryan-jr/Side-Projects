"""
[2/17/2012] Challenge #9 [easy]

write a program that will allow the user to input digits, and arrange them in numerical order.

for extra credit, have it also arrange strings in alphabetical order


https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/
"""

userData = []
userInput = input("Please input a number: ")
userData.append(int(userInput))

print("Type in 'xxx' to exit")

while userInput != "xxx":
  userInput = input("Please input a number: ")
  if userInput == "xxx":
    break
  userData.append(int(userInput))
  


print(sorted(userData))



