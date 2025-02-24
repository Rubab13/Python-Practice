# Output:
# A
# B B
# C C C
# D D D D
# E E E E E

list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
rows = int(input("Enter the number of rows: "))

if (rows <= 26):
  for i in range(0, rows):
    for j in range(0, i+1):
      print(list[i], end='')
    print()
else:
  print("Alphabet number out of range. Should be 26 or lower.")