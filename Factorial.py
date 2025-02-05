# Factorial of a number in python

def factorial():
  x = int(input("Enter a number: "))
  product = 1
  for i in range(x, 1, -1):
    product = product * i
  print(f"The factorial of {x} is {product}.")
  
factorial()