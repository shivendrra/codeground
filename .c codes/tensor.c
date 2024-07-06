#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  int *data;
  int *grad;
  int *shape;
  int ndim;
} Tensor;

Tensor *create_tensor(int *data, int *shape, int ndim) {
  Tensor *tensor = (Tensor*)malloc(sizeof(Tensor));
  tensor->data = data;
  tensor->shape = shape;
  tensor->ndim = ndim;
  tensor->grad = NULL;
  return tensor;
}

void print_tensor(Tensor *tensor) {
  int num_elements = 1;
  printf("[");
  for (int i = 0; i < tensor->ndim; i++) {
    num_elements *= tensor->shape[i];
  }

  for (int i = 0; i < num_elements; i++) {
    printf(" %d.0,", tensor->data[i]);
  }
  printf("]\n");
}

Tensor *add_tensor(Tensor *a, Tensor *b) {
  if (a->ndim != b->ndim) {
    printf("Shapes mismatch: Tensor a.shape %d != Tensor b.shape %d", a->shape, b->shape);
    return NULL;
  }
  
  for (int i = 0; i < a->ndim; i++) {
    if (a->shape[i] != b->shape[i]) {
      printf("Shapes mismatch: Tensor a.shape[%d] %d != Tensor b.shape[%d] %d\n", i, a->shape[i], i, b->shape[i]);
      return NULL;
    }
  }

  int num_elements = 1;
  for (int i = 0; i < a->ndim; i++) {
    num_elements *= a->shape[i];
  }
  
  int *result_data = (int*)malloc(num_elements * sizeof(int));
  for (int i=0 ; i < num_elements ; i++) {
    result_data[i] = a->data[i] + b->data[i];
  }

  return create_tensor(result_data, a->shape, a->ndim);
}

int main() {
  int data1[] = {1, 4, 0, 8};
  int shape1[] = {2, 2};
  Tensor *tensor1 = create_tensor(data1, shape1, 2);

  int data2[] = {0, 5, 7, 1};
  int shape2[] = {2, 2};
  Tensor *tensor2 = create_tensor(data2, shape2, 2);
  printf("tensor1: ");
  print_tensor(tensor1);
  printf("tensor2: ");
  print_tensor(tensor2);
  
  Tensor *result = add_tensor(tensor1, tensor2);
  printf("result tensor: ");
  print_tensor(result);

  free(tensor1);
  free(tensor2);
  free(result);
  return 0;
}