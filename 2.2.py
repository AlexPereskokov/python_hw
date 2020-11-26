print('Enter your sequence of numbers: ')
mas = [int(i) for i in input().split()]
for ind in range(1, len(mas), 2):
    mas[ind-1], mas[ind] = mas[ind], mas[ind-1]
print('Correct sequence: ')
print(' '.join([str(i) for i in mas]))
