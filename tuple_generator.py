# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# Tuple : ('3', ' 5', ' 7', ' 23')

string = input("Enter comma separated numbers: ")
print(tuple(string.split(",")))