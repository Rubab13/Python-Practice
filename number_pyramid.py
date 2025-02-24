# Output:
#     1
#    222
#   33333
#  4444444
# 555555555

rows = int(input("Enter the number of rows: "))

for i in range(1, rows+1):
  for j in range(i, rows):
    print(" ", end='')
  for j in range(0, i):
    print(i, end='')
  for j in range(0, i-1):
    print(i, end='')
  print()