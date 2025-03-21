# Write a function that returns all prime numbers up to n.

def findPrimeNumbers(n):
  result = []
  for i in range(2, n + 1):  # Start from 2, as 1 is not prime
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):  # Check divisibility up to sqrt(i)
      if i % j == 0:
        is_prime = False
        break
    if is_prime:
      result.append(i)
    
  return result

print(findPrimeNumbers(5))  # Output: [2, 3, 5]
print(findPrimeNumbers(10))  # Output: [2, 3, 5, 7]
print(findPrimeNumbers(1))  # Output: []