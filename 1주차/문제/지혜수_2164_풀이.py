import sys
from collections import deque

n = int(input())

arr = deque(range(n+1))
arr.popleft()

while len(arr)>1:
    arr.popleft()
    arr.append(arr.popleft())
    
print(arr[0])