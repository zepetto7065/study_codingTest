import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m) :
    line = list(map(int, sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1


def dfs(start, visited) :
    visited += [start]
    for c in range(len(matrix[start])) :
        if matrix[start][c] == 1 and (c not in visited) :
            dfs(c, visited)
    return visited


result = dfs(1, [])
print(len(result) - 1)
