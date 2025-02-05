# Find Maximum in a List

list = [1, 2, 3, 4, 5, 6]
max = list[0]

for i in range(0, len(list)):
  if (max < list[i]):
    max = list[i]
    
print(f"The largest number in the given list is {max}.")