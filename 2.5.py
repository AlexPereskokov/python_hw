my_list = [7, 5, 3, 3, 2]
new_elem = int(input("Enter new item: "))
place = -1
for i, el in enumerate(my_list):
    if new_elem > el:
        place = i
        break
if place == -1:
    my_list.append(new_elem)
else:
    my_list.insert(place, new_elem)
print('Your result: '+','.join(map(str, my_list))+'.')
