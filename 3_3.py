def max_mult():
    try:
        max = 0
        min = 0
        arg1 = int(input('Enter your first number: '))
        arg2 = int(input('Enter your second number: '))
        if arg2 > arg1:
            max = arg2
            min = arg1
        else:
            max = arg1
            min = arg2
        arg3 = int(input('Enter your third number: '))
        if arg3 > max or arg3 > min:
            result = arg3 + max
        else:
            result = min + max
    except ValueError:
        return 'Value error'
    return result


print(f'result is {max_mult()}')
