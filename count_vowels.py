# Count vowels in a string

string = input("Enter a string: ")
count = 0

for i in range(0, len(string)):
  if (string[i] in ['a', 'e', 'i', 'o', 'u']):
    count = count + 1
    
print(f"The vowels in the string {string} are {count}.")