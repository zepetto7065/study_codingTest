from collections import deque
que = deque()

N = int(input())
for i in range(1, N+1):
    que.appendleft(i)

while len(que) > 1:
    que.pop()
    que.appendleft(que.pop())

print(que[0])
