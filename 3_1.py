def div():
    try:
        arg1 = int(input("Input dividend "))
        arg2 = int(input("Input divider "))
        result = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"
    return result


print(f'result is {div()}')
