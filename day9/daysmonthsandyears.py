"""
Author: Carter Spenner
Date: 4/2/2026
Purpose: To practice using the datetime module and match statements in Python
"""

import datetime

# its all kinda a mess of 80% and 90% because of how you have to change the 80% to get a 90% so both
def leapyear (year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

month = 0
while not (month >= 1 and month <= 12):
    month = int(input("Enter the number of a month (1-12): "))
year = int(input("Enter a year: "))
inputtedDate = datetime.datetime(year=year, month=month, day=1)
print(f"The month you entered is: {inputtedDate.strftime('%B')}")


match month:
    case 4 | 6 | 9 | 11:
        print(f"There are 30 days in {inputtedDate.strftime('%B')}.")
    case 2 if leapyear(year):
        print(f"There are 29 days in {inputtedDate.strftime('%B')}.")
    case 2:
        print(f"There are 28 days in {inputtedDate.strftime('%B')}.")
    case _:
        print(f"There are 31 days in {inputtedDate.strftime('%B')}.")

#just 90% code
if leapyear(inputtedDate.year):
    print(f"{inputtedDate.year} is a leap year.")
else:
    print(f"{inputtedDate.year} is not a leap year.")

#100 code
birthday = datetime.datetime(year=2011, month=3, day=7, hour=7, minute=16)
currentDate = datetime.datetime.now()
timeAlive = currentDate - birthday
#this stuff is here twice because it asks for that in the instructions
print(f"I have been alive for {timeAlive.total_seconds()} seconds.")
print(f"I was born on a {birthday.strftime('%A')}.")
print(f"I was born on a {birthday.strftime('%A')} and have been alive for {timeAlive.total_seconds()} seconds.")