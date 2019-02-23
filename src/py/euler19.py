from datetime import date
import time

sundays = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		if date(year, month, 1).weekday() == 6:
			sundays += 1

start = time.time()			
answer = sundays
end = time.time()

total = end - start
print('Problem 19: ' + str(answer) + '\nDone in ' + str(total) + ' seconds.')

# Problem 19: 171
# Done in 7.152557373046875e-07 seconds.
