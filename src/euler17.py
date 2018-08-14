from num2words import num2words
import time

string = ''
for i in range(1, 1001):
  word = num2words(i)
  for char in word:
    if char != '-' and char != ' ':
      string += char

start = time.time()
answer = len(string)
end = time.time()

total = end - start
print('Problem 17: ' + str(answer) + '\nDone in ' + str(total) + ' seconds.')

# Problem 17: 21124
# Done in 3.0994415283203125e-06 seconds.
