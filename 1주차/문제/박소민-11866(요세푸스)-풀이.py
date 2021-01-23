from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())
one = deque()
result = []
for i in range(1, n+1):
    one.append(i)
while one:
    for _ in range(k-1):
        one.append(one.popleft())
    result.append(one.popleft())


print('<'+', '.join(map(str, result))+'>')
