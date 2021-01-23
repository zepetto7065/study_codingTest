from collections import deque

n, k = list(map(int, input().split()))

q = deque()
result = []
for i in range(1,n+1) :
    q.append(i)

for i in range(n) :
    if len(q) > 0 :
        if k <= len(q):
            print(q[k-1])
            q.remove(q[k-1])
            k += 2
            if k > len(q):
                k = k - len(q)
        else:
            break
#나머지
for _ in range(len(q)):
    print(q.popleft())

#출력

