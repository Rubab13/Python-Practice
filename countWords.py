# Write a Python program that asks the user for a sentence and counts how many words are in it.

sentence = input("Enter a sentence: ")
list = sentence.split()
print(f"The number of words in the given sentence are {len(list)}.")