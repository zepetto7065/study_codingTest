# small(50점)과 large(50점)로 나뉘어 있는데 점수 산정 기준을 모르겠습니다.

from collections import deque
deque = deque()
buffer = int(input())

while(True):
  k=int(input())
  if k == -1:
    break
  elif k == 0:
    deque.popleft()
  else:
    deque.append(k)

if (deque):
  for n in deque:
    print(n, end=" ")
else:
  print('empty')