from collections import deque

MAX = 100001
check = [False] * MAX
dist = [-1] * MAX

n, k = map(int, input().split())

check[n] = True
dist[n] = 0

q = deque()
q.append(n)

next_queue = deque()

while q:
    now = q.popleft()
    next = now * 2
    if next < MAX and check[next] is False:
        q.append(next)
        check[next] = True
        dist[next] = dist[now]

    next = now + 1
    if next < MAX and check[next] is False:
        next_queue.append(next)
        check[next] = True
        dist[next] = dist[now] + 1

    next = now - 1
    if next >= 0 and check[next] is False:
        next_queue.append(next)
        check[next] = True
        dist[next] = dist[now] + 1

    if not q:
        q = next_queue
        next_queue = deque()

print(dist[k])
