from collections import deque

import sys
input = sys.stdin.readline  # 보통 input을 사용하지만 시간단축을 위해 sys.stdin.readline를 사용
que = deque()
N = int(input())
for _ in range(N):
    a = list(map(str, input().split()))
    # input값을 공백기준으로 나눈 후, map을 통해 string형식으로 변환하고,
    # 그 값들을 list로 만들어준다.
    cmd = a[0]
    if cmd == 'push':
        que.append(a[1])
    elif cmd == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
