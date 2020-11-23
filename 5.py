print('Your first result:')
a=int(input())
print('Your final cause:')
b=int(input())
n_day=1
while a<b:
    r=a*0.1
    a+=r
    n_day+=1
print('Your will achieve result in:',n_day,'days')