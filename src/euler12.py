# Problem 12 - What is the value of the first triangle number to have over five hundred divisors?

def partialSum(n):
  res = 0
  res = (n*(n+1))/2
  return res

def countDivisors(n):
    result_set = set()
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    return len(result_set)
    
stop = 0
while stop == 0:
  for y in range(12375, 12376):
    res12 = 0
    res12 = countDivisors(partialSum(y))
    if res12 > 500 or res12 == 500:
      stop = 1 
      break

print('Answer for number 12 is : ' + str(partialSum(int(y))) + '\n')
