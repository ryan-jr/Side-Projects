"""
https://www.reddit.com/r/dailyprogrammer/comments/qit0h/352012_challenge_18_easy/
Often times in commercials, phone numbers contain letters so that they're easy to remember (e.g. 1-800-VERIZON). Write a program that will convert a phone number that contains letters into a phone number with only numbers and the appropriate dash. Click here to learn more about the telephone keypad.
Example Execution: Input: 1-800-COMCAST Output: 1-800-266-2278
"""

# Check if isnumber if not int pass, else from that index to -1 those are the letters you want
# Then pass that to the function and have the function map the letters to the numbers 
# Example Output: 1 - 800 - 837 - 4966 
dataInput = "1-800-VERIZON"
dataInput = list(dataInput)
ltrCount = 0

phoneList = ["A", 2, "B", 2, "C", 2, "D", 3, "E", 3, "F", 3, "G", 4, "H", 4, "I", 4, "J", 5, 
"K", 5, "L", 5, "M", 6, "N", 6, "O", 6, "P", 7, "Q", 7, "R", 7, "S", 7, "T", 8, "U", 8, 
"V", 8, "W", 9, "X", 9, "Y", 9, "Z", 9 ]

for i in dataInput:
  if i.isalpha() == True:
    x = phoneList.index(i)
    if ltrCount == 3:
      print(" -", phoneList[x + 1], end = "")
      ltrCount = -2
    else:
      print(phoneList[x + 1], end = "")
      ltrCount += 1
  elif i == "-":
      print(" - ", end = "")
  else:
      print(i, end = "")
