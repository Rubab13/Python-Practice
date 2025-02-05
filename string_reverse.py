# Reversing a string.

string = input("Enter a string: ")
new_string = ''

for i in range(len(string)-1, -1, -1):
  new_string = new_string + string[i]

print(f"The string {string} reversed is {new_string}.")