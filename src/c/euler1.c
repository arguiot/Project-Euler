// Project 1 - Find the sum of all the multiples of 3 or 5 below 1000

#include <stdio.h>
#include <stdlib.h>

double getSum (int maximum);

int main (int argc, char *argv[]) {
	int sum = getSum(1000);
	printf("%d\n", sum); 
	return EXIT_SUCCESS;
}

double getSum (int maximum) {
	int index = 0;
	int sum = 0;
	while (index < maximum) {
		if (((index % 3) == 0) || ((index % 5) == 0)) {
			sum = sum + index;
		}
		index++;
	}
	return sum;
}