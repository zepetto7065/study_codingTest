num = list(map(int, input().split()))

for i in range(1,len(num)):
    if num[i] < num[i-1]:
        num[i], num[i-1] = num[i-1], num[i]

for _ in num:
    print(_)