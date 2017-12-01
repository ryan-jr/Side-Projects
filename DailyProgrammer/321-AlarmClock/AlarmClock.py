# Setting up lists to access

tens = ["oh", "", "twenty", "thirty", "forty", "fifty"]

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "ninteen"]
 
# Setting up neccessary variables   
final_str = ["It's"]
time = "21:00"
hour = int(time[:2])
mins = int(time[3:5])


# Checking through the hour and appending as neccessary

if (hour == 0) and (mins == 0):
    
    final_str.append(ones[11]) 
elif hour == 0:
    
    final_str.append(ones[11])
elif hour < 10:
    
    final_str.append((ones[hour - 1]))
elif hour > 12:
    
    final_str.append((ones[hour - 13]))


# Checking through minutes and appending as neccessary

if mins == 0:
    final_str.append("")
      
elif mins == (20 or 30 or 40 or 50):
    
    final_str.append(tens[mins // 10])
elif mins < 10:
    
    final_str.append((tens[0]))
    final_str.append((ones[mins - 1]))
elif (mins < 20) and (mins >= 10):
    
    final_str.append((tens[1]))
    final_str.append((ones[mins - 11]))
elif (mins < 30) and (mins >= 20):
    
    final_str.append(tens[2])
    final_str.append(ones[mins - 21])
elif (mins < 40) and (mins >= 30):
    
    final_str.append(tens[3])
    final_str.append(ones[mins - 31])
elif (mins < 50) and (mins >= 40):
    
    final_str.append(tens[4])
    final_str.append(ones[mins - 41])
elif (mins < 60) and (mins >= 50):
    
    final_str.append(tens[5])
    final_str.append(ones[mins - 51])

    
    
# Adding AM or PM
if hour < 12:
    
    final_str.append("AM")
else:
    
    final_str.append("PM")
    
print(" ".join(final_str))



