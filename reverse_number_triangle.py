# Output:
# 12345
# 1234
# 123
# 12
# 1

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
  for j in range(1, i+1):
    print(j, end='')
  print()