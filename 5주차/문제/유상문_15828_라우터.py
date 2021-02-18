import sys
from collections import deque


n = int(sys.stdin.readline())
q = deque()

while True :
    command = int(sys.stdin.readline())

    if len(q) <= n and command != -1 :
        if command == 0 :
            q.popleft()
        elif len(q) < n :
            q.append(command)
    else :
        break

for _ in q :
    if len(q) == 0 :
        print('empty')
    else:
        print(_, end=' ')