# Check if the given number is even or odd.

number = int(input("Enter a number: "))
    
if number <= 0:
  print("Please enter a positive number.")
else:
  if (number % 2 == 0):
    print(f"The number {number} is an even number.")
  else:
    print(f"The number {number} is an odd number.")