a=int(input())
max=a%10
a=a//10
while a > 0:
    if a%10>max:
        max=a%10
    a=a//10
print("max)
