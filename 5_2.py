my_f = open(r"C:\Users\User\Desktop\test_file.txt", "r", encoding='utf-8')
count_str = 0
for line in my_f:
    count_str += 1
    count_wrd = len(line.split())
    print(f'Line number {count_str} contains {count_wrd} word(s)')
print('Total number of lines', count_str)
my_f.close()
