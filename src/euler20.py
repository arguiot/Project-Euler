import time

def factorial(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  
  return res
  
def sum_digits(n):
  ln = list(str(n))
  res = 0
  for i in ln:
    res += int(i)
  
  return res

start = time.time()
answer = sum_digits(factorial(100))
end = time.time()

total = end - start
print('Problem 20: ' + str(answer) + '\nDone in ' + str(total) + ' seconds.')

# Problem 20: 648
# Done in 8.487701416015625e-05 seconds.
