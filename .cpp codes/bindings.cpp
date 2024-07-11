#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "tensor.h"

namespace py = pybind11;

PYBIND11_MODULE(tensorlib, m) {
  py::class_<Tensor, std::shared_ptr<Tensor>>(m, "Tensor")
    .def(py::init<const std::vector<double>&, const std::vector<size_t>&, bool>(),
      py::arg("data"), py::arg("shape"), py::arg("requires_grad") = true)
    .def(py::init<const std::vector<double>&, bool>(),
      py::arg("data"), py::arg("requires_grad") = true)
    .def_readonly("data", &Tensor::data)
    .def_readonly("shape", &Tensor::shape)
    .def_readonly("ndim", &Tensor::ndim)
    .def_readonly("requires_grad", &Tensor::requires_grad)
    .def_readonly("grad", &Tensor::grad)
    .def_readonly("strides", &Tensor::strides)
    .def_readonly("size", &Tensor::size)
    .def("backward", &Tensor::backward)
    .def("get_shape", &Tensor::get_shape);
}
