# Problem 9 - A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

# Find the product abc.

l = 335
m = 334
n = 1000 - l - m
while n + m + l != 1000 or n**2 + m**2 != l**2:
    if n > m or m == 2:
        l += 1
        m = l - 1
    m -= 1
    n = 1000 - l - m
result9 = m*n*l 
print("Answer for problem 9 is : " + "\n" + str(result9) + "\n")
