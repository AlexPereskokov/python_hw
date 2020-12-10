from functools import reduce


list_ch = [el for el in range(100, 1001, 2)]
sum = reduce(lambda x, y: x*y, list_ch)
print(f'Sum of even numbers in the range: {sum}')
