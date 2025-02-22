# Write a Python program that asks the user for a number and prints the multiplication table for that number up to 10.

number = int(input("Enter a number: "))
for i in range(1, 11):
  print(f"{number} * {i} = {number*i}")