"""

https://www.reddit.com/r/dailyprogrammer/comments/qit0h/352012_challenge_18_easy/

Often times in commercials, phone numbers contain letters so that they're easy to remember (e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters into a phone number with only numbers and the appropriate dash. Click here to learn more about the telephone keypad.

Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278
"""

def letterToNumber(letters):
  pass 



# Check if isnumber if not int pass, else from that index to -1 those are the letters you want
# Then pass that to the function and have the function map the letters to the numbers 
dataInput = "1-800-COMCAST"
dataInput = list(dataInput)

for i in dataInput:
  if i.isnumeric() == True or i == "-":
    pass
  else:
    print(i)
