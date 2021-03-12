import sys
from collections import deque
MAX = 10001
check = [False] * MAX
dist = [-1] * MAX
n, k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

result = 0
while q :
    now = q.popleft()

    if now == k :
        result = dist[now]
        break
    if now * 2 <= MAX and check[now*2] == False :
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 <= MAX and check[now+1] == False :
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now -1 >= 0 and check[now-1] == False:
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1
print(result)