import time

# Problem 4 - Find the largest palindrome made from the product of two 3-digit numbers

# 100 * 100 = 10 000 and 999 * 999 = 998 001  --> largest palindrome  --> ex : 20002 is not the largest palindrome ---> the largest palindrome is a 6 digits number.
# The palindrome can be written as:

# abccba

# So we have :

# 100000a + 10000b + 1000c + 100c + 10b + a

# That is :

# 100001a + 10010b + 1100c

# Factoring out 11, it is equivalent to :

# 11(9091a + 910b + 100c)

# So the palindrome must be divisible by 11. 

start = time.time()
d = 0  
for e in range(999, 100, -1):  
    for f in range(e, 100, -1):  
        x = e * f 
        if x > d and x%11 == 0:  
            s = str(e * f)  
            if s == s[::-1]:  
                d = e * f  
end = time.time()
totalt = end - start

print("Answer for problem 4 is : " + "\n" + str(d) + "\n" + 'Done with repl.it in : ' + str(totalt))
