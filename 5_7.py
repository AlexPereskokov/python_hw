import json

my_f = open(r"C:\Users\User\Desktop\test_file.txt", "r", encoding='utf-8')
profit = {}
pr = {}
full_list = []
prof = 0
i = 0
for line in my_f:
    name, firm, earning, damage = line.split()
    damage = damage[:len(damage)-1]
    profit[name] = int(earning) - int(damage)
    if profit.setdefault(name) >= 0:
        prof += profit.setdefault(name)
        i += 1
if i != 0:
    prof = prof / i
pr = {'average_profit': round(prof)}
full_list.append(profit)
full_list.append(pr)
my_f_js = open('test_file.json', 'w')
json.dump(full_list, my_f_js)
my_f.close()
my_f_js.close()
