num = list(map(int , input().split()))

for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j] = num[j],num[i]

for _ in num:
    print(_)