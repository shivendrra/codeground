// Tensor.cpp
#include "tensor.h"
#include <numeric>
#include <algorithm>

Tensor::Tensor(const std::vector<double>& data, const std::vector<size_t>& shape, bool requires_grad)
  : data(data), shape(shape), requires_grad(requires_grad) {
  init();
}

Tensor::Tensor(const std::vector<double>& data, bool requires_grad)
  : data(data), shape({data.size()}), requires_grad(requires_grad) {
  init();
}

void Tensor::init() {
  ndim = shape.size();
  strides = calculate_strides(shape);
  size = calculate_size(shape);
  if (requires_grad) {
    grad = std::make_shared<Tensor>(std::vector<double>(size, 0.0), shape, false);
  }
  _backward = [](){};
}

std::vector<size_t> Tensor::calculate_strides(const std::vector<size_t>& shape) {
  std::vector<size_t> strides(shape.size());
  strides[shape.size() - 1] = 1;
  for (int i = shape.size() - 2; i >= 0; --i) {
    strides[i] = strides[i + 1] * shape[i + 1];
  }
  return strides;
}

size_t Tensor::calculate_size(const std::vector<size_t>& shape) {
  return std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<size_t>());
}

std::vector<size_t> Tensor::get_shape() const {
  return shape;
}

void Tensor::backward() {
  _backward();
}