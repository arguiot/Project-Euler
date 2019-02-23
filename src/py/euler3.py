import time 
# Project 3 - What is the largest prime factor of the number 600851475143 ?

def lpf(c):  # largest_prime_factor
    u = 2
    while u * u <= c:
        if c % u:
            u += 1
        else:
            c //= u            # c // i returns the integer quotient of c/i 
    return c

#import scikit-learn

start = time.time()
res3 = lpf(600851475143)
end = time.time()
totalt = end - start

print("Answer for problem 3 is : " + "\n" + str(res3) + "\n" + 'Done with repl.it in : ' + str(totalt))
