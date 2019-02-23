import time

# Using the central binominal coeficient

def factorial(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  
  return res

def for_grid(sz):
  return int(factorial(2 * sz) / factorial(sz)**2)
  
start = time.time()
answer = for_grid(20)
end = time.time()

total = end - start
print('Problem 15: ' + str(answer) + '\nDone in ' + str(total) + ' seconds.')
    
# Problem 15: 137846528820
# Done in 2.7179718017578125e-05 seconds.
