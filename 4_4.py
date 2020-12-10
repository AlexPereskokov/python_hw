first_list = input('Enter your string of numbers: ').split()
new_list = [el for el in first_list if first_list.count(el) < 2]
print("Unique number list: ", ' '.join(map(str, new_list)))
