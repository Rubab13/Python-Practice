# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

rows = int(input("Enter the number of rows: "))
number = 1

for i in range(0, rows):
  for j in range(0, i+1):
    print(number, end=' ')
    number+=1
  print()