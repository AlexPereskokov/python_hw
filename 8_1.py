class Date:
    def __init__(self, line) -> None:
        self._str = line

    @classmethod
    def number(cls, line):
        num_date = line.split('-')
        return int(num_date[0]), int(num_date[1]), int(num_date[2])

    @staticmethod
    def valid(line):
        error_message = ''
        is_correct = True
        day, month, year = Date.number(line)
        if not 1 <= day <= 31:
            error_message += 'Wrong day '
            is_correct = False
        if not 1 <= month <= 12:
            error_message += 'Wrong month '
            is_correct = False
        if not 2021 >= year >= 0:
            error_message += 'Wrong year'
            is_correct = False
        return 'All are correct' if is_correct else error_message

    def __str__(self) -> str:
        return f'Your date is {Date.number(self._str)}'


today = Date('11-1-2001')
print(today)
print(Date.valid('13-55-2020'))
print(today.number('15-1-2010'))
print(Date.valid('12-22-43'))
