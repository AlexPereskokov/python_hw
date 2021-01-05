from abc import *


class Clothes(ABC):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    @abstractmethod
    def square(self):
        pass

    def __str__(self) -> str:
        return f'Fabrics for clothing are necessary {self.square}'


class Coat(Clothes):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    @property
    def square(self):
        return round(self.width / 6.5 + 0.5)


class Jacket(Clothes):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

    @property
    def square(self):
        return round(self.height * 2 + 0.3)


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(f'Summary fabrics = {jacket.square + coat.square}')
