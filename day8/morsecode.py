"""
Author: Carter Spenner
Date: 4/1/2026
Purpose: To practice using dictionaries in Python
"""

morse_code = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
}

#80% code
print(f"P in morse code: {morse_code['P']}")

#90% code
word1 = input("Enter a word to convert to Morse code (letters only, must be uppercase): ")

for letter in word1:
    if letter == " ":
        print("/ ", end="")
    else:
        print(morse_code[letter], end="")

#100% code
word2 = input("\nEnter another word to convert to Morse code (letters only, upper or lower): ")

for letter in word2.upper():
    if letter == " ":
        print("/ ", end="")
    else:
        print(morse_code[letter], end="")