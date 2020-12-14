my_f = open(r"C:\Users\User\Desktop\test_file.txt", "r", encoding='utf-8')
my_dict = {}
for line in my_f:
    sum = 0
    sub, hours = line.split(':')
    for hour in hours.split():
        if hour != '—':
            sum += int(hour[:hour.find('(')])
    my_dict.setdefault(sub, sum)
print(my_dict)
