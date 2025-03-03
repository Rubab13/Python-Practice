# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

number = input("Enter a number: ")
result = int(number) + int(number + number) + int(number + number + number)
print("Result:", result)