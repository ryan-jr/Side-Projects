# Find the first recurring character in a string 


# 1: Accept user input as a string (they may input numbers/other stuff, but it should be a string)
# 2: Slice the string at the first character, compare the first character to each subsequent character and try to find a match.  If there is a match stop, if not, use the second character in the search.  

# Accepting Inputs
user_data = '*l1J?)yn%R[}9~1"=k7]9;0[$'

# Loop through each character, step through it and stop when a match is found
for i in user_data:
  user_data = user_data[1::1]
  if user_data.find(i) != -1:
    print(i)
    break



    
  