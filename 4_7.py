from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


n = int(input('Enter a finite number of factorial: '))
cnt = 0
for i in fact():
    if cnt < n:
        print(i, end=' ')
        cnt += 1
    else:
        break
