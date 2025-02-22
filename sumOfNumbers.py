# Write a Python program that asks the user for a number and prints the sum of all numbers from 1 to that number.

number = int(input("Enter a number: "))
sum = 0
for i in range(1, number+1):
  sum = sum + i
print(f"The sum of numbers from 1 to {number} is {sum}.")