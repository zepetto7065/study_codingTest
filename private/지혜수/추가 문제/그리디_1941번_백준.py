import sys

n = int(sys.stdin.readline())
arr = []
last = 0
answer = 0

for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for x in arr:
  if last <= x[0]:
    answer += 1
    last = x[1]

print(answer)