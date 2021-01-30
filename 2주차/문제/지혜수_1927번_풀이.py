import sys
import heapq

n = int(sys.stdin.readline())
h = []
for _ in range(n):
  k = int(sys.stdin.readline())
  if k == 0:
    if(len(h)!=0):
      print(heapq.heappop(h))
    else:
      print(0)
  else:
    heapq.heappush(h, k)