import numpy as np
import tensor

class Tensor:
    def __init__(self, data, dtype=None):
        self.data = np.array(data, dtype=dtype)
        self.shape = list(self.data.shape)
        self.dtype = self.data.dtype
        self.c_tensor = tensor.Tensor(self.data.flatten().tolist(), self.shape)

    def add(self, other):
        result_c_tensor = self.c_tensor.add(other.c_tensor)
        result_data = result_c_tensor.get_data()
        result_shape = result_c_tensor.get_shape()
        result_array = np.array(result_data).reshape(result_shape)
        return Tensor(result_array, dtype=self.dtype)

    def sum(self):
        return self.c_tensor.sum()

    def get_item(self, indices):
        return self.c_tensor.get_item(indices)

    def __repr__(self):
        return f"Tensor(data={self.data}, dtype={self.dtype})"

if __name__ == "__main__":
    t1 = Tensor([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
    t2 = Tensor([[5.0, 6.0], [7.0, 8.0]], dtype=np.float32)

    print("Tensor 1:")
    print(t1)

    print("Tensor 2:")
    print(t2)

    t3 = t1.add(t2)
    print("Sum of Tensor 1 and Tensor 2:")
    print(t3)

    print("Sum of elements in Tensor 1:")
    print(t1.sum())
