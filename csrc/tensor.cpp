#include <iostream>
#include "tensor.h"

Tensor::Tensor(const TensorData& data, const std::vector<size_t>& shape)
    : data(data), shape(shape) {
    ndim = shape.size();
    size = calculate_size(shape);
    strides = calculate_strides(shape);
    verify_data_size();
}

size_t Tensor::calculate_size(const std::vector<size_t>& shape) const {
    return std::accumulate(shape.begin(), shape.end(), 1, std::multiplies<size_t>());
}

std::vector<size_t> Tensor::calculate_strides(const std::vector<size_t>& shape) const {
    std::vector<size_t> strides(shape.size());
    strides.back() = 1;
    for (int i = shape.size() - 2; i >= 0; --i) {
        strides[i] = strides[i + 1] * shape[i + 1];
    }
    return strides;
}

void Tensor::verify_data_size() const {
    std::visit([this](const auto& vec) {
        if (vec.size() != size) {
            throw std::runtime_error("Data size does not match shape size");
        }
    }, data);
}

size_t Tensor::calculate_flat_index(const std::vector<size_t>& indices) const {
    if (indices.size() != ndim) {
        throw std::runtime_error("Number of indices does not match tensor dimensions");
    }
    size_t index = 0;
    for (size_t i = 0; i < ndim; ++i) {
        index += indices[i] * strides[i];
    }
    return index;
}

size_t Tensor::get_size() const {
    return size;
}

const std::vector<size_t>& Tensor::get_shape() const {
    return shape;
}

size_t Tensor::get_ndim() const {
    return ndim;
}

template<typename T>
T Tensor::sum() const {
    return std::visit([](const auto& vec) {
        using VecType = std::decay_t<decltype(vec)>;
        return std::accumulate(vec.begin(), vec.end(), static_cast<typename VecType::value_type>(0));
    }, data);
}

template<typename T>
T Tensor::get_item(const std::vector<size_t>& indices) const {
    size_t index = calculate_flat_index(indices);
    return std::visit([index](const auto& vec) -> T {
        return static_cast<T>(vec[index]);
    }, data);
}

Tensor Tensor::add(const Tensor& other) const {
    if (shape != other.shape) {
        throw std::runtime_error("Shapes do not match for addition");
    }

    return std::visit([this, &other](const auto& vec1, const auto& vec2) -> Tensor {
        using VecType = std::decay_t<decltype(vec1)>;
        VecType result(vec1.size());

        for (size_t i = 0; i < vec1.size(); ++i) {
            result[i] = vec1[i] + vec2[i];
        }

        return Tensor(result, shape);
    }, data, other.data);
}

// Explicit template instantiation
template int Tensor::sum<int>() const;
template float Tensor::sum<float>() const;
template double Tensor::sum<double>() const;

template int Tensor::get_item<int>(const std::vector<size_t>& indices) const;
template float Tensor::get_item<float>(const std::vector<size_t>& indices) const;
template double Tensor::get_item<double>(const std::vector<size_t>& indices) const;

std::vector<float> Tensor::get_data() const {
    return std::get<std::vector<float>>(data);
}

int main() {
    // Create some tensor data
    std::vector<float> data1 = {1.0, 2.0, 3.0, 4.0};
    std::vector<float> data2 = {5.0, 6.0, 7.0, 8.0};
    std::vector<size_t> shape = {2, 2};

    // Create Tensor objects
    Tensor tensor1(data1, shape);
    Tensor tensor2(data2, shape);

    // Print tensor details
    std::cout << "Tensor 1 shape: ";
    for (const auto& dim : tensor1.get_shape()) {
        std::cout << dim << " ";
    }
    std::cout << "\n";

    std::cout << "Tensor 2 shape: ";
    for (const auto& dim : tensor2.get_shape()) {
        std::cout << dim << " ";
    }
    std::cout << "\n";

    // Perform addition
    Tensor tensor_sum = tensor1.add(tensor2);

    // Print sum tensor details
    std::cout << "Sum Tensor shape: ";
    for (const auto& dim : tensor_sum.get_shape()) {
        std::cout << dim << " ";
    }
    std::cout << "\n";

    std::cout << "Sum Tensor elements: ";
    for (size_t i = 0; i < tensor_sum.get_size(); ++i) {
        std::cout << tensor_sum.get_item<float>({i / 2, i % 2}) << " ";
    }
    std::cout << "\n";

    return 0;
}