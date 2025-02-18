rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
  for j in range(0, i):
    print(" ", end='')
  for k in range(rows, i, -1):
    print("*", end='')
  print()