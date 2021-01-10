class NotIntException(Exception):
    pass


my_list = []
stop = False
while not stop:
    data = input().split()
    for d in data:
        try:
            if d == 'stop':
                stop = True
                break
            if not d.isdigit():
                raise NotIntException
        except NotIntException:
            print("Your enter is not digit")
        else:
            my_list.append(int(d))
print(my_list)
