# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']

string = input("Enter comma separated numbers: ")
print(string.split(","))