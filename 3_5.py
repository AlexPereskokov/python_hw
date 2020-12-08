def my_sum ():
    sum_res = 0
    ex = True
    spec = '!'
    while ex:
        number = input('Input numbers or ! for quit - ').split()
        res = 0
        for el in number:
            if el == spec:
                ex = False
                break
            else:
                res = res + int(el)
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')


my_sum()
