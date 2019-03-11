// Project 1 - Find the sum of all the multiples of 3 or 5 below 1000

// Use the sum function to print the sum of multiples of a number contained by a bigger number n ; sum(number multiple, bigger number n)

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double sum(double multiples, double a) {
  return multiples * floor((a - 1.0) / multiples) * (floor((a - 1.0) / multiples) + 1.0) / 2.0;
}

int main (int argc, char *argv[]) {
  clock_t begin = clock();
  
  double res1 = sum(3.0, 1000.0) + sum(5.0, 1000.0) - sum(15.0, 1000.0);
  
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
  
  printf("Answer for problem 1 is : \n%f \nDone with repl.it in %f", res1, time_spent);

  return EXIT_SUCCESS;
}
