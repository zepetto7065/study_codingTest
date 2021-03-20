from collections import deque

computer_count = int(input())
link_count = int(input())

links = [[] for _ in range(computer_count + 1)]
check = [False] * (computer_count + 1)

for _ in range(link_count):
    u, v = map(int, input().split())
    links[u].append(v)
    links[v].append(u)

for i in range(computer_count + 1):
    links[i].sort()


def dfs(x):
    check[x] = True
    for y in links[x]:
        if check[y] is False:
            dfs(y)


dfs(1)
print(len(list(filter(lambda x: x is True, check))) - 1)

# def bfs(start):
#     q = deque()
#     q.append(start)
#     check[start] = True
#
#     while q:
#         x = q.popleft()
#
#         for y in links[x]:
#             if check[y] is False:
#                 check[y] = True
#                 q.append(y)
#
# bfs(1)
# print(len(list(filter(lambda x: x is True, check))) - 1)
