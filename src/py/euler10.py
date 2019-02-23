# Problem 10 - Find the sum of all the primes below two million.

res10 = 0
from sympy import prime
for i in range(1,2000000):
  if prime(i) > 2000000:
    break
  res10 += prime(i)

print("Answer for problem 10 is : " + "\n" + str(res10) + '\n')
