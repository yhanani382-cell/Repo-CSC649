# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#CSC649: My first Python experiment
sentence = input("Enter a sentence: ")
if sentence.strip() == "": print("You did not enter a sentence.")
else:
    word_count = len(sentence.split())
character_count = len(sentence)
print("Word count:", word_count)
print("Character count (including spaces):", character_count)