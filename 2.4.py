word_list = [str(i) for i in input().split()]
for num, el in enumerate(word_list):
    if len(el) > 10:
        print(f" {num+1} {el[0:10]}")
    else:
        print(f" {num+1} {el}")
