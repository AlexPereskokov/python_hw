num = int(input('Enter the number of products: '))
goods = []
for i in range(num):
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))
    value = int(input('Enter quantity of goods: '))
    unit = input('Enter unit of measure: ')
    goods.append(
        (i + 1, {
            'name': name,
            'price': price,
            'value': value,
            'unit': unit
        })
    )
stats = {}
for good in goods:
    for info in good[1].keys():
        value = good[1][info]
        if info not in stats:
            stats[info] = []
        if value not in stats[info]:
            stats[info].append(value)
from pprint import pprint

pprint(goods)
pprint(stats)
