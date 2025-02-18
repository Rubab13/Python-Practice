rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
  for j in range(rows-1, i, -1):
    print(" ", end='')
  for k in range(0, i+1):
    print("*", end='')
  for l in range(0, i):
    print("*", end='')
  print()