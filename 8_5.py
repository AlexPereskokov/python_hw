class ComplexNumber:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Sum z1 and z2 equal')
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)

    def __mul__(self, other):
        print(f'Multiplication z1 and z2 equal')
        a = self.a * other.a - (self.b * other.b)
        b = self.b * other.a
        return ComplexNumber(a, b)

    def __str__(self) -> str:
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 * z_2)
print(z_1 + z_2)
