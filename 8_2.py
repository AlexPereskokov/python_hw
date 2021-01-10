class DivisionByNull(Exception):
    pass


try:
    divider = int(input())
    denominator = int(input())
    if denominator == 0:
        raise DivisionByNull
    print(divider/denominator)
except DivisionByNull:
    print('Impossible to divide by zero')
