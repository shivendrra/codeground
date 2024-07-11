#include <iostream>
#include <vector>
#include <stdexcept>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <functional>
#include <type_traits>

template <typename T>
class Array {
public:
  using ValueType = T;
  using Container = std::vector<T>;

  Array(std::initializer_list<T> init_list) : data(init_list), dtype(get_dtype()) {
    update_shape();
  }

  Array(const Container& init_data) : data(init_data), dtype(get_dtype()) {
    update_shape();
  }

  Array(const Array& other) : data(other.data), shape(other.shape), ndim(other.ndim), dtype(other.dtype) {}

  Array& operator=(const Array& other) {
    if (this != &other) {
      data = other.data;
      shape = other.shape;
      ndim = other.ndim;
      dtype = other.dtype;
    }
    return *this;
  }

  friend std::ostream& operator<<(std::ostream& os, const Array& arr) {
    if (arr.ndim == 1) {
      os << "Array([";
      for (size_t i = 0; i < arr.data.size(); ++i) {
        os << arr.data[i];
        if (i < arr.data.size() - 1) os << ", ";
      }
      os << "], dtype=" << arr.dtype << ")";
    } else {
      os << "Array([";
      for (size_t i = 0; i < arr.data.size(); ++i) {
        os << arr.data[i];
        if (i < arr.data.size() - 1) os << ",\n\t";
      }
      os << "], dtype=" << arr.dtype << ")";
    }
    return os;
  }

  T& operator()(std::initializer_list<size_t> indices) {
    if (indices.size() != ndim) throw std::invalid_argument("Invalid number of indices");
    size_t index = 0;
    size_t multiplier = 1;
    for (auto it = indices.end(); it != indices.begin();) {
      --it;
      index += (*it) * multiplier;
      multiplier *= shape[it - indices.begin()];
    }
    return data[index];
  }

  void reshape(std::initializer_list<size_t> new_shape) {
    size_t total_size = std::accumulate(new_shape.begin(), new_shape.end(), 1, std::multiplies<size_t>());
    if (total_size != data.size()) throw std::invalid_argument("Total size of new array must be unchanged");
    shape = new_shape;
    ndim = shape.size();
  }

  size_t num_elements() const {
    return data.size();
  }

  const Container& to_vector() const {
    return data;
  }

  Array transpose() const {
    if (ndim != 2) throw std::invalid_argument("Only 2D arrays can be transposed");
    size_t rows = shape[0], cols = shape[1];
    Array result(std::vector<T>(cols * rows));
    for (size_t i = 0; i < rows; ++i) {
      for (size_t j = 0; j < cols; ++j) {
        result.data[j * rows + i] = data[i * cols + j];
      }
    }
    result.shape = { cols, rows };
    result.ndim = 2;
    return result;
  }

private:
  Container data;
  std::vector<size_t> shape;
  size_t ndim;
  std::string dtype;
  std::string get_dtype() const {
    if (std::is_same<T, int8_t>::value) return "int8";
    if (std::is_same<T, int16_t>::value) return "int16";
    if (std::is_same<T, int32_t>::value) return "int32";
    if (std::is_same<T, int64_t>::value) return "int64";
    if (std::is_same<T, float>::value) return "float32";
    if (std::is_same<T, double>::value) return "float64";
    return "unknown";
  }

  void update_shape() {
    shape = { data.size() };
    ndim = 1;
  }
};

int main() {
  Array<int> array1({1, 2, 3, 4, 5});
  Array<double> array2({1.1, 2.2, 3.3, 4.4, 5.5});

  std::cout << array1 << std::endl;
  std::cout << array2 << std::endl;
  
  return 0;
}