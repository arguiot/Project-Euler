# Problem 6 - Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumsquare(upto):      # Sum of all square numbers up to a number 
  sumn1 = 0
  for compteur in range(upto + 1):
    sumn1 += compteur**2 
  return sumn1 


def squaresum(upton):    # Square of the sum of every number up to a number
  sumn2 = 0
  for compteur2 in range(upton + 1):
    sumn2 += compteur2 
  return sumn2**2

print("Answer for problem 6 is :" )
print(str(squaresum(100) - sumsquare(100)) + '\n')
