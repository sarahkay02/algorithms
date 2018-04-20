#include <iostream>
using namespace std;

// determine if an integer is odd
int isOdd(int n) {
  return (n & 1) != 0;
}

//use isOdd() and print out resulting values
int main() {
  for (int i=-5; i<6; i++) {
    cout << i << " " << isOdd(i) << endl;
  }
  return 0;
}
