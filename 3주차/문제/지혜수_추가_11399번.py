import sys

n = int(sys.stdin.readline())
answer = 0

arr = sorted(list(map(int, sys.stdin.readline().split())))

for x in arr:
    answer += x*(n)
    n -= 1

print(answer)