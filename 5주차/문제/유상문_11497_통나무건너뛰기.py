
import heapq
import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n) :
    length = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(numbers)
    q = deque()
    for i in range(length) :
        if i % 2 == 0 :
            q.append(numbers[i])
        else :
            q.appendleft(numbers[i])
    dif = []
    for i in range(0, length - 1) :
        dif.append(abs(q[i + 1] - q[i]))  # 절대값

    heapq.heapify(dif)
    print(dif[length - 2])
