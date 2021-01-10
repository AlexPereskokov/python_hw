class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price': self.price, 'Count': self.quantity}

    def __str__(self) -> str:
        return f'{self.name} price is {self.price} count are/is {self.quantity}'

    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        # while True:
        try:
            unit = input(f'Enter model')
            unit_p = int(input(f'Enter price '))
            unit_q = int(input(f'Enter count '))
            unique = {'Model': unit, 'Price': unit_p, 'Count': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Incorrect enter'

        print(f'For exit - Exit, For continue - Enter')
        q = input(f'---> ')
        if q == 'Exit':
            self.my_store_full.append(self.my_store)
            print(f'All store -\n {self.my_store_full}')
            return f'Exit'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self) -> str:
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self) -> str:
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self) -> str:
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
