import sys
t = int(input())

for _ in range(t):
    n = int(input())
    num = []

    for i in range(n):
        p = list(map(int, sys.stdin.readline().split()))
        num.append(p)
    num.sort()
    max_num = 1
    min = num[0][1]
    for i in range(1, n):
        if num[i][1] < min:
            min = num[i][1]
            max_num += 1

    print(max_num)
