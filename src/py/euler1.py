# Project 1 - Find the sum of all the multiples of 3 or 5 below 1000

# Use the sum function to print the sum of multiples of a number contained by a bigger number n ; sum(number multiple, bigger number n)

from math import floor
import time

def sum(multiples, a):
  return multiples * floor((a - 1.0) / multiples) * (floor(( a - 1.0) / multiples) + 1.0) / 2.0

start = time.time()
res1 = sum(3.0, 1000.0) + sum(5.0, 1000.0) - sum(15.0, 1000.0)
end = time.time()
totalt = end - start

print("Answer for problem 1 is : " + "\n" + str(res1) + "\n" + 'Done with repl.it in : ' + str(totalt))

