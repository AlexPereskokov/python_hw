def sqr_fun(a1, a2):
    try:
        res = a1 ** a2
    except ValueError:
        return 'Value error'
    return res


def sqr_fun1(a1, a2):
    try:
        res = 1
        for _ in range(abs(a2)):
            res /= a1
    except ValueError:
        return 'Value error'
    return res


arg1 = int(input('Enter your first positive number: '))
arg2 = int(input('Enter your second negative number: '))
print(f'result is {sqr_fun(arg1, arg2)}')
print(f'result is {sqr_fun1(arg1, arg2)}')
