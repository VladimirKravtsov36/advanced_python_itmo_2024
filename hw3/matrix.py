import numpy as np

class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Incompatible matrices dimensions")
        return Matrix(self.array + other.array)

    def __mul__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Incompatible matrices dimensions")
        return Matrix(self.array * other.array)

    def __matmul__(self, other):
        if self.array.shape[1] != other.array.shape[0]:
            raise ValueError("Incompatible matrices dimensions")
        return Matrix(self.array @ other.array)

    def __str__(self):
        return str(self.array)

def save_to_file(filename, matrix):
    with open(filename, "w") as f:
        f.write(str(matrix))

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    add_result = matrix1 + matrix2
    mul_result = matrix1 * matrix2
    matmul_result = matrix1 @ matrix2
    
    save_to_file("artifacts/3.1/matrix+.txt", add_result)
    save_to_file("artifacts/3.1/matrix*.txt", mul_result)
    save_to_file("artifacts/3.1/matrix@.txt", matmul_result)