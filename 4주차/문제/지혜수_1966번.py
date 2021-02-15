from collections import deque
import sys

a = int(sys.stdin.readline())

for _ in range(a):
  n, idx = map(int, sys.stdin.readline().split())
  arr = deque(map(int, sys.stdin.readline().split()))
  cnt = 0
  while (True):
    tmp = arr.popleft() 
    if idx == 0:
      if len(arr)==0 or tmp >= max(arr):
        cnt += 1
        print(cnt)
        break
      else:
        arr.append(tmp)
        idx = len(arr)-1
    else:
      if len(arr)==0 or tmp >= max(arr):
        cnt += 1
      else:
        arr.append(tmp)
      idx -= 1