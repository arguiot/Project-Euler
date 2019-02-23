// Project 2 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

#include <stdio.h>
#include <stdlib.h>

#define FOUR_MILLION 4000000

int sumEvenFibonacci();

int main (int argc, char *argv[]) {
  int sum = 0;
  sum = sumEvenFibonacci();
  printf("%d\n", sum);
  return EXIT_SUCCESS;
}

int sumEvenFibonacci() {
  int sum = 0;
  int a = 1;
  int b = 1;
  while (b < FOUR_MILLION) {
    a = a + b;
    b = b + a;
    if (b%2 == 0) {
      sum = sum + b;
    }
  }
  return sum;
}
