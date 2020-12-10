from sys import argv


name, time, salary, bonus = argv

print('Name of script: ', name)
print('Your time: ', time)
print('Your salary: ', salary)
print('Your bonus: ', bonus)


def res(t, s, b):
    try:
        r = t * s + b
        print(f'The final salary is:  {r}')
    except ValueError:
        print('Not a number')


res(int(time), int(salary), int(bonus))
