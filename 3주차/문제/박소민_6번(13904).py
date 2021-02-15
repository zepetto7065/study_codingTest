import sys
n = int(input())
alist = []
score = 0

for _ in range(n):
    a, b = map(int, input().split(" "))
    alist.append((a, b))

alist = sorted(alist, key=lambda x: -x[1])
Maxsum = [0 for i in range(1001)]

for i in range(len(alist)):
    x = alist[i][0]
    y = alist[i][1]
    for x in range(x, 0, -1):
        if Maxsum[x] == 0:
            Maxsum[x] = y
            break

print(sum(Maxsum))
