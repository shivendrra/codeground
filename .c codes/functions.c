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
  return 0;
}

// int temp(int fahr){
//   int cel;
//   cel = 5 * (fahr - 32) / 9;
//   return cel;
// }

// int main(){
//   int lower, step, upper, fahr, cel;
//   lower = 0;
//   step = 20;
//   upper = 300;

//   fahr = lower;
//   while(fahr <= upper){
//     cel = temp(fahr);
//     printf("%d fahrenheit in celcius: %d\n", fahr, cel);
//     fahr = fahr + step;
//   }
//   return 0;
// }