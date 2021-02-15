# import sys
# sys.stdin = open("input.txt", "r")
n = int(input())

for _ in range(n):
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    index = [0 for _ in range(n)]
    index[m] = 1
    cnt = 0
    while True:
        if max(a) == a[0]:
            cnt += 1
            if index[0] == 1:
                print(cnt)
                break
            else:
                a.pop(0)
                index.pop(0)
        else:
            a.append(a.pop(0))
            index.append(index.pop(0))
