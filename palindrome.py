word = input("Enter a word: ")
newWord = ""
for i in range(0, len(word)):
  newWord = word[i] + newWord
if (word == newWord):
  print("The given word is a palindrome.")
else:
  print("The given word is not a palindrome.")