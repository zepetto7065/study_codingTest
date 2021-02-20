from collections import deque
import sys
# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())
que = deque()
while True:
    a = int(sys.stdin.readline())
    if a == -1:
        break
    else:
        if a == 0:
            que.popleft()
        elif len(que) < n:
            que.append(a)

if len(que) != 0:
    for i in que:
        print(i, end=' ')
else:
    print("empty")
