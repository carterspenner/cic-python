"""
Author: Carter Spenner
Date: 3/25/2026
Purpose: Practice utilizing lists in Python.
"""
import random
loop = True

#80% SECTION

#create the initial list
movies = ["Despicable Me", "The Matrix", "The Lord of the Rings", "The Lion King", "The Minecraft Movie", "The Lego Movie"]
print(movies)

#add a movie
movies.append("The Lego Movie 2")
print(movies)

#change a movie
movies[0] = "Despicable Me 2"
print(movies)

#remove a movie
movies.remove("The Matrix")
print(movies)

#sort movies
movies.sort()
print(movies)


#90%/100% SECTION

#define magic 8 ball answers
answers = ["Yes", "No", "Maybe", "Ask again later", "Definitely not", "Absolutely", "Without a doubt", "It is certain", "Very doubtful", "Outlook not so good"]

#ask for user's name and greet them
username = input("What is your name?: ")
print(f"Hello, {username}! Welcome to the Magic 8 Ball!")

#ask user for question in a loop until they choose to stop
while loop:
    question = input("What is your question for the Magic 8 Ball? (must be a yes or no):\n")
    print(f"The Magic 8 Ball says... {random.choice(answers)}")
    if input("Do you want to ask another question? (y/n): ").lower() != "n":
        loop = True
    else:
        loop = False
    