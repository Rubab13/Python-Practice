# Output:
# * * * * 
#  * * * *
# * * * * 
#  * * * *

rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
  if not (i%2 == 0):
    print(" ", end='')
  for j in range(0, rows): 
    print("* ", end='')
  print()