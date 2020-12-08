def max_mult(a1, a2, a3):
    try:
        max = 0
        min = 0
        if a2 > a1:
            max = a2
            min = a1
        else:
            max = a1
            min = a2
        if a3 > max or a3 > min:
            result = a3 + max
        else:
            result = min + max
    except ValueError:
        return 'Value error'
    return result


arg1 = int(input('Enter your first number: '))
arg2 = int(input('Enter your second number: '))
arg3 = int(input('Enter your third number: '))
print(f'result is {max_mult(arg1, arg2, arg3)}')
