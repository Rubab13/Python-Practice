# Remove duplicates from a list

list = [1, 2, 3, 4, 5, 5]
unique_list = []

for num in list:
  if num not in unique_list:
    unique_list.append(num)
    
print("The unique list is:", unique_list)