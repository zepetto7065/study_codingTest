# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque
n, m, start = map(int, input().split())

links = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    links[u].append(v)
    links[v].append(u)

print(links)

for i in range(n + 1):
    links[i].sort()
print(links)


def dfs(x):
    check[x] = True
    print(x, end=' ')
    for y in links[x]:
        if check[y] == False:
            dfs(y)


def bfs(start):
    check = [False] * (n + 1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in links[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)


dfs(start)
print()
bfs(start)
print()
