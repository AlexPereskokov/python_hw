my_f = open("random_file.txt", "w")
while True:
    b = input("Enter something: ")
    if b != '':
        my_f.write(f'{b}\n')
    else:
        break
my_f.close()
