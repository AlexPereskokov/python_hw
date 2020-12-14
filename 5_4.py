my_f = open(r"C:\Users\User\Desktop\test_file.txt", "r", encoding='utf-8')
my_new_f = open("random_file.txt", "w")
tr_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for line in my_f:
    num, _, dig = line.split()
    ru_num = tr_dict.get(num)
    my_new_f.write(f'{ru_num} - {dig}\n')
my_f.close()
my_new_f.close()
