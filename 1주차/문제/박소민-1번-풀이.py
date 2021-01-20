import sys
input = sys.stdin.readline
a = []
N = int(input())
for _ in range(N):
    n = list(map(str, input().split()))  # 예시 n = [push,1], map(변환 함수, 데이터)

    go = n[0]
    if go == "push":
        a.append(n[1])
    elif go == "pop":
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif go == "size":
        print(len(a))
    elif go == "empty":
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif go == "top":
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])
