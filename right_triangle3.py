rows = int(input("Enter the number of rows: "))

for i in range(0, rows+1):
  for j in range(rows, i, -1):
    print(" ", end='')
  for k in range(0, i):
    print("*", end='')
  print()