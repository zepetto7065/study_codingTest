# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
from collections import deque

#동그라미..? 큐
saw = deque()
list = []
#4개의 톱니바퀴 입력
for _ in range(4):
    saw.append()
# n = int(input())

for _ in range(2):
    number, dir = input().split() # 톱니바퀴 번호, 방향

    #정방향
    if dir == 1 :
        if list[number-1][2] != list[number][2]:
            print('123')
    #역방향
