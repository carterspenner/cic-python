"""
Author: Carter Spenner
Date: 3/25/2026
Purpose: Practice utilizing while loops in Python.
"""

import random
n = 0
keepRolling = True

#80% code
#makes sure that even if input is a float, it will be converted to an integer by truncating the decimal part
number = int(float(input("Enter a number: ")) // 1)

while n < number:
    print("While loop")
    n += 1

#90% code
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
while keepRolling:
    print(f"You rolled a {die1} and a {die2}.")
    if input("Would you like to roll again? (y/n) ").lower() != "y":
        keepRolling = False
    else:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

#100% code
number1 = int(float(input("Enter a number: ")) // 1)
number2 = int(float(input("Enter another number, larger than the first: ")) // 1)
while number1 <= number2:
    print(number1)
    number1 += 1