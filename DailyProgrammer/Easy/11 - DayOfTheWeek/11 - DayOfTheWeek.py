"""
The program should take three arguments. The first will be a day, the second will be month, and the third will be year. Then, your program should compute the day of the week that date will fall on.



https://www.reddit.com/r/dailyprogrammer/comments/pwons/2192012_challenge_11_easy/
"""
import datetime
import calendar


userDate = input("Please input a date in the format of YYYY/MM/DD")
year, month, day = map(int, userDate.split("/"))
date1 = datetime.date(year, month, day)


# Python formatting starts "day 0" with Monday
# print(datetime.datetime.weekday(date1))

# Getting a day of the week in a readable format
print(calendar.day_name[date1.weekday()])
