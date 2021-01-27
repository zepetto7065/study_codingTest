from collections import deque

n = int(input())
q = deque()

# N장의 카드 생성
for i in range(1, n + 1):
    q.append(i)

for _ in range(n):
    if len(q) > 1 :
        q.popleft()

    if len(q) == 1:
        print(q.popleft())
        break
    else:
        q.append(q.popleft())
