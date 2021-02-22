# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1
import sys

n,m = map(int, input().split())
r, c, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change(d) :
    if d== 0: #북
        return 3
    elif d == 1: #동
        return 0
    elif d == 2: #남
        return 1
    elif d == 3: #서
        return 2

def solution(r, c, d) :
    cnt = 1
    x = r
    y = c
    map[x][y] = 2

    while True:
        dc = d
        for i in range(4):
            empty = 0
            dc = change(dc)
            nx = x + dx[dc]
            ny = y + dy[dc]
            #유효범
            if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0 :
                cnt += 1
                x = nx
                y = ny
                map[nx][ny] = 2
                d = dc
                empty = 1
                break

        #4방향 청소
        if empty == 0 :
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2 :
                x -= 1
            elif d ==3 :
                y += 1
            if map[x][y] == 1:
                break
    return cnt


print(solution(r,c,d))
