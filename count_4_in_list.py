# Write a Python program to count the number 4 in a given list.

list = []
count = 0

number = int(input("Enter the number you want to search in the list: "))
size = int(input("What is the size of the list: "))
for i in range(0, size):
  num = int(input("Enter the number: "))
  list.append(num)

for i in range(0, len(list)):
  if (list[i] == number):
    count = count + 1
    
print(f"The number of times {number} appears in the list is {count}.")