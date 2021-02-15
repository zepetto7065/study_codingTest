import sys

n = int(sys.stdin.readline())
d = {}
for i in range(n):
  tmp = list(map(int, sys.stdin.readline().split()))
  day = tmp[0]
  while day > 0:
    if day not in d.keys():
      d[day] = tmp[1]
      break
    elif d[day] < tmp[1]:
      d[day], tmp[1] = tmp[1], d[day]
    day-=1
print(sum(d.values()))