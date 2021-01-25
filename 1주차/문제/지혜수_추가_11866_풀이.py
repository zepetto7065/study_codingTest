import sys
from collections import deque

n, k = map(int, input().split())
queue = deque(range(1,n+1))
answer = []
while len(answer)!=n:
  for i in range(k):
    if i == (k-1):
      answer.append(queue.popleft())
    else:
      queue.append(queue.popleft())

print('<'+', '.join(map(str,answer))+'>')