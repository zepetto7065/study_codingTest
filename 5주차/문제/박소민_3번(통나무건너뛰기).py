from collections import deque

n = int(input())
for _ in range(n):
    que = deque()
    length = int(input())
    all_list = list(map(int, input().split(' ')))
    all_list.sort()
    que.append(all_list.pop())
    for i in range(length-2, -1, -1):
        if i % 2 == 0:
            que.appendleft(all_list.pop())
        else:
            que.append(all_list.pop())
    max_num = 0
    for i in range(length-1):
        if abs(que[i+1]-que[i]) > max_num:
            max_num = abs(que[i+1]-que[i])
    print(max_num)
