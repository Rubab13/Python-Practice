rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
  for j in range(0, rows):
    if (j == 0 or j == rows-1 or i == 0 or i == rows-1):
      print("*", end='')
    else:
      print(" ", end='')
  print()