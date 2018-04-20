#include <stdio.h>

// determine if an integer is odd
int isOdd(int n) {
  return (n & 1) != 0;
}

// use isOdd() and print out results
int main(void) {
  for (int i=-5; i<6; i++) {
    printf("%d %d\n", i, isOdd(i));
  }
}
