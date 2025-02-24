# Output:
#     *    
#    * *   
#   *   *  
#  *     * 
# *********

rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
  for j in range(i, rows-1):
    print(" ", end='')
  for j in range(0, i+1):
    if (j == 0 or i == rows-1):
      print("*", end='')
    else:
      print(" ", end='')
  for j in range(0, i):
    if (j == i-1 or i == rows-1):
      print("*", end='')
    else:
      print(" ", end='')
  print()