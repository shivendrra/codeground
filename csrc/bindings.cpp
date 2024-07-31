#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "tensor.h"

namespace py = pybind11;

PYBIND11_MODULE(tensor, m) {
  py::class_<Tensor>(m, "Tensor")
    .def(py::init<const std::vector<float>&, const std::vector<size_t>&>())
    .def("get_size", &Tensor::get_size)
    .def("get_shape", &Tensor::get_shape)
    .def("get_ndim", &Tensor::get_ndim)
    .def("sum", &Tensor::sum<float>)
    .def("get_item", &Tensor::get_item<float>)
    .def("add", &Tensor::add)
    .def("get_data", &Tensor::get_data);
}