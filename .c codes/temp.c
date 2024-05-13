#include <stdio.h>

/*
  for far-cel table
  for fahr = 0, 20, 40, ...., 300
*/

int main(){
  int fahr, cel;
  int lower, step, upper;

  lower = 0;
  upper= 300;
  step = 20;

  fahr = lower;
  while(fahr <= upper){
    cel = 5 * (fahr-32) / 9;
    printf("%d\t%d\n", fahr, cel);
    fahr = fahr + step;
  }
}