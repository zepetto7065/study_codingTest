from collections import deque

n, k = list(map(int, input().split()))
start_k = k
q = deque()
result = deque()
for i in range(1,n+1) :
    q.append(i)

for _ in range(n):
    if start_k < len(q):
        result.append(q[k-1])
        q.remove(q[k-1])

        k += start_k - 1

        if k > len(q):
            k = k - len(q)
    else:
        break
#나머지
for _ in range(len(q)):
    result.append(q.popleft())

#출력
print('<'+', '.join(map(str, result))+'>')

# 풀이에 오류가 있습니다. 소민님 풀이를 참고바랍니다.