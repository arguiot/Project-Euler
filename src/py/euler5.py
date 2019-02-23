import time 

# Problem 5 - What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(n1, n2):
  if ( n1 == n2 ): 
    return n1;
  while (n2 != 0):
        r  = n1 % n2
        n1 = n2
        n2 = r
  else:
    return n1

# lcm calculation from wiki

def lcm(n1,n2):
  return int( n1 * n2 / gcd(n1,n2) )

# lcm(1..10) = lcm(lcm(1..9),10)  
# now computing lcm(1..20)

t = 1
start = time.time()
for i in range(2, 21):
  t = lcm(i, t)
end = time.time()
totalt = end - start

print("Answer for problem 5 is : " + "\n" + str(t) + "\n" + 'Done with repl.it in : ' + str(totalt))
