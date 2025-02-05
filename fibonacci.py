# Print fibonacci series

def fibonacci():
  number = int(input("Enter a number: "))
    
  if number <= 0:
    print("Please enter a positive number.")
    return
  elif number == 1:
    print(0)
    return
  elif number == 2:
    print(0, 1)
    return
    
  first, second = 0, 1
  print(first, second, end=" ")

  for _ in range(number - 2):
    next_term = first + second
    print(next_term, end=" ")
    first, second = second, next_term

fibonacci()
