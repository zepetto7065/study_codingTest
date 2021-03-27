# DFS, BFS 모두 가능
# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque
m = int(input())
n = int(input())


links = [[] for _ in range(m + 1)]
check = [False] * (m + 1)
for _ in range(n):
    x, y = map(int, input().split())
    links[x].append(y)
    links[y].append(x)

for i in range(m + 1):
    links[i].sort()


def dfs(x):
    check[x] = True
    for y in links[x]:
        if check[y] == False:
            cnt.append(y)
            dfs(y)


# def bfs(start):
#     cnt = 0
#     q = deque()
#     q.append(start)
#     check[start] = True
#     while q:
#         cnt += 1
#         x = q.popleft()
#         for y in links[x]:
#             if check[y] == False:
#                 check[y] = True
#                 q.append(y)
#     print(cnt-1)

cnt = []
dfs(1)
print(len(cnt))
