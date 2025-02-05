# Check if the given number is prime or not.

number = int(input("Enter a number: "))
    
if number < 2:
  print(f"{number} is not a prime number.")
else:
  count = 0
  for i in range(1, number+1):
    if (number % i == 0):
      count = count + 1
      if (count > 2):
        break
  
  if (count == 2):
    print(f"The number {number} is a prime number.")
  else:
    print(f"The number {number} is not a prime number.")