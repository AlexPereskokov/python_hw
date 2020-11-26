print('Enter your proceeds:')
proc=int(input())
print('Enter your costs:')
cos=int(input())
prof=proc-cos
if prof>0:
    print('Your positive profit is:',prof)
    effi=(prof/proc)*100
    print('Enter the number of employees:')
    num=int(input())
    num_prof=prof/num
    print('Your profitability is:',effi)
    print('Profit per employee:',num_prof)
elif prof==0:
    print('Your profit is:',prof)
else:
    print('Your negative profit is:',prof)
