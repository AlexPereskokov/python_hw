def div(a1, a2):
    try:
        result = a1 / a2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    return result


arg1 = int(input("Input dividend "))
arg2 = int(input("Input divider "))
print(f'result is {div(arg1,arg2)}')
