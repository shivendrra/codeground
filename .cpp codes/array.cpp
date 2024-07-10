#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int array1[] = {1, 5, 2, 6, 8, 3, 45};
  int n = sizeof(array1) / sizeof(array1[0]);

  cout<< "[";
  for (int i=0; i < n; i++) {
    cout<< " " << array1[i] << ",";
  }
  cout<< "]";
  cout<<endl<<endl;

  int array2[2][3] = {{1, 5, 7}, {1, 6, 7}};
  int x = sizeof(array2) / sizeof(array2[0]);
  int y = sizeof(array2[0]) / sizeof(array2[0][1]);

  cout<< "["<< endl;
  for (int i=0; i < x; i++) {
    cout<< "  [";
    for (int j=0; j < y; j++) {
      cout<< " " << array2[i][j] << ",";
    }
    cout<< "]" << endl;
  }
  cout<< "]";
  
  return 0;
}