from typing import List


class Matrix:
    _data: List[List[int]] = None

    def __init__(self, data: List[List[int]]) -> None:
        self._data = data

    def __str__(self) -> str:
        return '\n'.join(' '.join(str(element) for element in row) for row in self._data)

    def __add__(self, other: 'Matrix') -> 'Matrix':
        summary = [[other._data[row_i][i] + self._data[row_i][i] for i, _ in enumerate(row)] for row_i, row in enumerate(self._data)]
        return Matrix(summary)


m = Matrix([[1, 2], [1, 2]])
print(m)
m1 = Matrix([[2, 1], [2, 1]])
print(m1+m)
