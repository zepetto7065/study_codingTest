import heapq
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
import sys

n = int(sys.stdin.readline())
list = []
while n > 0 :
    num = int(sys.stdin.readline())
    if num > 0 :
        heapq.heappush(list, num)
    elif num ==0 :
        if len(list) > 0:
            heapq.heapify(list)
            print(heapq.heappop(list))
        else :
          print(0)
    n -= 1
