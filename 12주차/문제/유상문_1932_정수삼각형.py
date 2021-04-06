import sys

n = int(sys.stdin.readline())
t = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = 2

for i in range(1, n):
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1
print(max(t[n - 1]))