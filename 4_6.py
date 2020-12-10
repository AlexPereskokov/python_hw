from itertools import count, cycle


stop_el = int(input('You cycle is endless, enter end element: '))
for el in count(int(input('Enter start element: '))):
    if el > stop_el:
        break
    else:
        print(el, end=' ')
print('')
my_list = [False, 55.5, 666, None]
count = 0
stop_el = int(input('You cycle is endless, enter number of cycle repetitions: '))
for el in cycle(my_list):
    count += 1
    if count > (stop_el * len(my_list)):
        break
    else:
        print(el, end=' ')
