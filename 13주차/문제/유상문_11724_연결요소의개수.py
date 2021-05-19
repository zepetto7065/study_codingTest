N,M = map(int , input().split())
visited = [False for _ in range(N+1)]
target = [[] for _ in range(N+1)]
count = 0

for _ in range(M):
    u, v = map(int,input().split())
    target[u].append(v)
    target[v].append(u)


def dfs(i) :
    visited[i] = True
    for next in target[i]:
        if not visited[next]:
            dfs(next)


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
