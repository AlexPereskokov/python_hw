my_f = open(r"C:\Users\User\Desktop\test_file.txt", "r", encoding='utf-8')
av_sal = 0
count_prs = 0
for line in my_f:
    prs, sal = line.split()
    av_sal += sal
    count_prs += 1
    if int(sal) < 20:
        print(f'{prs} has a salary of less than 20 thousands')
av_sal = av_sal / count_prs
print('The average salary is', av_sal)
my_f.close()
