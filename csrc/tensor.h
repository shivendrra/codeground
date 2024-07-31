#ifndef TENSOR_H
#define TENSOR_H

#include <vector>
#include <variant>
#include <numeric>
#include <stdexcept>

using TensorData = std::variant<std::vector<int>, std::vector<float>, std::vector<double>>;

class Tensor {
public:
    Tensor(const TensorData& data, const std::vector<size_t>& shape);
    size_t get_size() const;
    const std::vector<size_t>& get_shape() const;
    size_t get_ndim() const;

    template<typename T>
    T sum() const;

    template<typename T>
    T get_item(const std::vector<size_t>& indices) const;

    Tensor add(const Tensor& other) const;

private:
    TensorData data;
    std::vector<size_t> shape;
    std::vector<size_t> strides;
    size_t ndim;
    size_t size;

    size_t calculate_size(const std::vector<size_t>& shape) const;
    std::vector<size_t> calculate_strides(const std::vector<size_t>& shape) const;
    void verify_data_size() const;
    size_t calculate_flat_index(const std::vector<size_t>& indices) const;
};

#endif