import numpy as np


class FileWriteMixin:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.array))

class StrMixin:
    def __str__(self):
        return str(self.array)

class GetterSetterMixin:
    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        self._array = value

class ArrayOps(FileWriteMixin, StrMixin, GetterSetterMixin):

    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Incompatible matrices dimensions")
        return ArrayOps(self.array + other.array)

    def __mul__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Incompatible matrices dimensions")
        return ArrayOps(self.array * other.array)

    def __matmul__(self, other):
        if self.array.shape[1] != other.array.shape[0]:
            raise ValueError("Incompatible matrices dimensions")
        return ArrayOps(self.array @ other.array)

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = ArrayOps(np.random.randint(0, 10, (10, 10)))
    matrix2 = ArrayOps(np.random.randint(0, 10, (10, 10)))

    add_result = matrix1 + matrix2
    mul_result = matrix1 * matrix2
    matmul_result = matrix1 @ matrix2
    
    add_result.save_to_file("artifacts/3.2/matrix+.txt")
    mul_result.save_to_file("artifacts/3.2/matrix*.txt")
    matmul_result.save_to_file("artifacts/3.2/matrix@.txt")