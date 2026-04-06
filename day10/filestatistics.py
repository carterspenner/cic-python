"""
Author: Carter Spenner
Date: 4/6/2026
Purpose: Learn how to read and write files using Python
"""

#80% code
import os

with open("day10/file.txt") as f: # open the file and read the contents, from terminal base directory
    contents = f.read()

wordCount = len(contents.split())
print(f"Word Count: {wordCount}")

lineCount = len(contents.splitlines())
print(f"Line Count: {lineCount}")

#90% code
charCount = len(contents.strip())
print(f"Character Count: {charCount}")

averageWPL = wordCount / lineCount
print(f"Average Words Per Line: {averageWPL}")

#100% code

word_dict = {}
for word in contents.lower().split():
    word = word.strip(",.")
    if len(word) > 0 and word != ".":
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

print("Top 3 Most Common Words:")
topThreeWords = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)[:3]
for word, count in topThreeWords:
    print(f"{word}: {count}")

with open("day10/output.txt", "w") as o:
    o.write(f"Word Count: {wordCount}\n")
    o.write(f"Line Count: {lineCount}\n")
    o.write(f"Character Count: {charCount}\n")
    o.write(f"Average Words Per Line: {averageWPL}\n")
    o.write("Top 3 Most Common Words:\n")
    for word, count in topThreeWords:
        o.write(f"{word}: {count}\n")