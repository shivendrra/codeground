#pragma once
#include <vector>
#include <set>
#include <functional>
#include <memory>

class Tensor {
public:
  std::vector<double> data;
  std::vector<size_t> shape;
  size_t ndim;
  bool requires_grad;
  std::shared_ptr<Tensor> grad;
  std::set<std::shared_ptr<Tensor>> prev;
  std::function<void()> _backward;
  std::string dtype;
  std::vector<size_t> strides;
  size_t size;

  Tensor(const std::vector<double>& data, const std::vector<size_t>& shape, bool requires_grad=true);
  Tensor(const std::vector<double>& data, bool requires_grad=true);

  void backward();
  std::vector<size_t> calculate_strides(const std::vector<size_t>& shape);
  size_t calculate_size(const std::vector<size_t>& shape);
  std::vector<size_t> get_shape() const;

private:
  void init();
};