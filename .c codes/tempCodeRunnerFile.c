#include <stdio.h>

int power(int base, int n){
  int i, p;
  p = 1;
  for(i=1; i<=n; ++i)
    p = p * base;
  return p;
}

int main(){
  int i;
  for (i=0; i<10; ++i)
    printf("i: %d, output1: %d, output2: %d\n", i, power(2,i), power(-3,i));
}