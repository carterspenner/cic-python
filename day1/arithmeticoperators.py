"""
Author: Carter Spenner
Date: 3/22/2026
Purpose: To demonstrate the use of arithmetic operators in Python.
"""

num1 = 4
num2 = 7

#Adds num1 and num2
print(f"Addition: {num1 + num2}")
#Subtracts num2 from num1
print(f"Subtraction: {num1 - num2}")
#Multiplies num1 and num2
print(f"Multiplication: {num1 * num2}")
#Divides num1 by num2
print(f"Division: {num1 / num2}")
#Returns the remainder of num1 divided by num2
print(f"Modulus: {num1 % num2}")
#Returns num1 raised to the power of num2
print(f"Exponentiation: {num1 ** num2}")
#Returns the floor of the division of num1 by num2
print(f"Floor Division: {num1 // num2}")

#Unsure if "enter a whole number between 2 and 9" means use input() or just assign a variable, so I will do both.

num3 = int(float(input("Enter a whole number between 2 and 9: ")) // 1)  #Using input and floor division to get a whole number.
print(f"You entered: {num3}")
num4 = num3 * 2
print(f"{num3} * 2 = {num4}")
num5 = num4 + 5
print(f"{num4} + 5 = {num5}")
num6 = num5 * 50
print(f"{num5} * 50 = {num6}")

if input("Has your birthday occurred this year? (yes/no): ").strip().lower() == "yes":
    num7 = num6 + 1776
    print(f"{num6} + 1776 = {num7}")
else:
    num7 = num6 + 1775
    print(f"{num6} + 1775 = {num7}")

yearOfBirth = int(input("What year were you born?: "))
num8 = num7 - yearOfBirth
print(f"{num7} - {yearOfBirth} = {num8}")

num9 = num8 % 100

print(f"{num8} % 100 = {num9}")