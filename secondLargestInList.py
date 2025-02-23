# Second largest number in a list

def secondLargestNumber(list):
  if (len(list) == 0):
    print("List is empty.")
    return
  max = secondLargest = list[0]
  for i in range(1, len(list)):
    if (list[i] > max):
      secondLargest = max
      max = list[i]
  print("The second largest number in the given list is ", end='')
  return secondLargest
  
print(secondLargestNumber([1, 2, 3, 4, 5]))
print(secondLargestNumber([]))
print(secondLargestNumber([100, 200, 300, 400, 500]))
print(secondLargestNumber([11, 22, 33, 44, 55, 66, 77, 88, 99]))