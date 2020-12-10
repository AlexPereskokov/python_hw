first_list = input('Enter your string of numbers: ').split()
new_list = [el for ind, el in enumerate(first_list) if ind > 0 and first_list[ind] > first_list[ind-1]]
print('Correct string is:', ' '.join(map(str, new_list)))
