a=int(input())
sec=a%60
hour=int(a/3600)
min=int((a/60)%60)
A=[hour,min,sec]
p=0
for i in A:
    if i==0:
        A[p]=str(00)
    elif i<=9:
        A[p]=str(0)+str(i)
    p+=1
print(':'.join(map(str, A)))
