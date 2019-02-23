import time 

# Project 2 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

# Use the fibupto function to list the Fibonacci sequence inferior to a number : fibupto(maximum number)

def fibupto(b):
  listfibupto = [0]
  n1, n2 = 0 ,1
  while n2 < b:
    n1, n2 = n2, n1 + n2
    listfibupto.append(n1)
  return "List of the Fibonacci sequence with terms inferior to " + str(b) + " : " + str(listfibupto)

# import time
# time.sleep(2)  --> sleep 2 seconds

print("This is a test : " + "\n" + str(fibupto(21)) + "\n")

# Use the fibn function to list a certain number of terms in the Fibonacci sequence : fibn(number of terms)

def fibn(nterms):
  listfibn = []
  t1, t2 = 0, 1 
  for i in range(nterms):
    t1, t2 = t2, t1 + t2 
    listfibn.append(t1)
  return print("List of " + str(nterms) + " terms of the Fibonacci sequence : " + "\n" + str(listfibn))
print("This is another test :")
fibn(14)

# Use the fibeven(limit) function to print the sum of every even term of the Fibonacci sequence : fibeven(maximum number)

def fibeven(limit):
	x, y = 1, 1
	total = 0
	while y < limit:
		total += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return total
start = time.time()
res2 = fibeven(4000000)
end = time.time()
totalt = end - start

print("\n" + "Answer for problem 2 is : " + "\n" + str(res2) + "\n" + 'Done with repl.it in : ' + str(totalt))
