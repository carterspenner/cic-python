"""
Author: Carter Spenner
Date: 3/23/2026 (yes I know it's earlier than we got this assigned)
Purpose: to practice using strings and inputs
"""

print("----Chatbot----\n")
name = str(input("What is your name?:\n"))
print(f"Hello, {name}!")

#Three Questions
question1 = str(input("What is your favorite color?:\n"))
print(f"Your favorite color is {question1}, {name}!\n")
question2 = str(input("What is your favorite animal?:\n"))
print(f"Your favorite animal is {question2}, {name}!\n")
question3 = str(input("What is your favorite food?:\n"))
print(f"Your favorite food is {question3}, {name}!\n\n")

print(f"So, {name}, your favorite color is {question1}, your favorite animal is {question2}, and your favorite food is {question3}.\n")

#Random Word Manipulation
print("----Random Word Manipulation----\n")
randomWord = str(input("Type a random word:\n"))
print(randomWord.upper())
print(randomWord.lower())
print(randomWord.replace("a", "x"))
print(f"{randomWord[1:len(randomWord)]}\n")

#Madlibs
#I'm using a publicly available template from https://madlibs.com/wp-content/uploads/2024/06/VacationFun_ML_2009_pg15.pdf
print("----MadLibs----\n")

noun1 = str(input("Type a noun:\n"))
noun2 = str(input("Type another noun:\n"))
noun3 = str(input("Type a noun again:\n"))
noun4 = str(input("Type a final noun:\n"))

adj1 = str(input("Type an adjective:\n"))
adj2 = str(input("Type another adjective:\n"))
adj3 = str(input("Type a final adjective:\n"))

pnoun1 = str(input("Type a plural noun:\n"))
pnoun2 = str(input("Type another plural noun:\n"))

game1 = str(input("Type a game:\n"))

verbing1 = str(input("Type a verb ending in -ing:\n"))
verbing2 = str(input("Type another verb ending in -ing:\n"))
verbing3 = str(input("Type a verb ending in -ing again:\n"))
verbing4 = str(input("Type a final verb ending in -ing:\n"))


plant1 = str(input("Type a plant:\n"))

place1 = str(input("Type a place:\n"))

number1 = str(input("Type a number:\n"))

bodypart1 = str(input("Type a body part:\n"))

print(f"A vacation is when you take a trip to some {adj1} place with your {adj2} family. Usually you go to some place that is near a/an {noun1} or up on a/an {noun2}. A good vacation place is one where you can ride {pnoun1} or play {game1} or go hunting for {noun3}. I like to spend my time {verbing1} or {verbing2}. When parents go on a vacation, they spend their time eating three {pnoun1} a day, and fathers play golf, and mothers sit around {verbing3}. Last summer, my little brother fell in a/an {noun4} and got poison {plant1} all over his {bodypart1}. My family is going to go to (the) {place1}, and I will practice {verbing4}. Parents need vacations more than kids because parents are always very {adj3} and because they have to work {number1} hours every day all year making enough {pnoun2} to pay for the vacation.")