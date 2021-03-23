num = list(map(int, input().split()))

for end in range(1, len(num)):
    for i in range(end,0,-1):
        if num[i-1] > num[i]:
            num[i-1], num[i] = num[i], num[i-1]

for _ in num:
    print(_)