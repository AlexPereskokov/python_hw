def info(n, s, b, c, e, p):
    return ' '.join([n, s, b, c, e, p])


name = input('Enter your name: ')
surname = input('Enter your surname: ')
birth = input('Enter your year of birth: ')
city = input('Enter your city: ')
email = input('Enter your email: ')
phone = input('Enter your phone: ')
print(f'Info about you: {info(n = name,s = surname,b = birth,c = city,e = email,p = phone)}')
