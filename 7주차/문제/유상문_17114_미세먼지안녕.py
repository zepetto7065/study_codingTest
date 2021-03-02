# def makeDust() :
#     for i in range(r) :
#         for j in range(c) :
#             if map[i][j] != -1 :
#                 mount = map[i][j] // 5  # 확산
#                 # 2번확산
#                 if i == 0 and j == 0 :
#                     dusts[1][0] += mount
#                     dusts[0][1] += mount
#                     count = 2
#                 elif i == 0 and j == c :
#                     dusts[1][c - 1] += mount
#                     dusts[r - 1][c] += mount
#                     count = 2
#                 elif i == r and j == 0 :
#                     dusts[0][c - 1] += mount
#                     dusts[1][c] += mount
#                     count = 2
#                 elif i == r and j == c :
#                     dusts[r - 1][c] += mount
#                     dusts[r][c - 1] += mount
#                     count = 2
#                 # 3번 확산
#                 elif 0 < i < r and j == 0 :
#                     dusts[i - 1][0] += mount
#                     dusts[i + 1][0] += mount
#                     dusts[i][1] += mount
#                     count = 3
#                 elif 0 < j < c and i == 0 :
#                     dusts[0][j - 1] += mount
#                     dusts[0][j + 1] += mount
#                     dusts[1][j] += mount
#                     count = 3
#                 elif 0 < i < r and j == c :
#                     dusts[i - 1][c] += mount
#                     dusts[i + 1][c] += mount
#                     dusts[i][c - 1] += mount
#                     count = 3
#                 elif 0 < j < c and i == r :
#                     dusts[r][j - 1] += mount
#                     dusts[r][j + 1] += mount
#                     dusts[r - 1][j] += mount
#                     count = 3
#                 # 4번확산
#                 else :
#                     dusts[i - 1][j + 1] += mount
#                     dusts[i + 1][j + 1] += mount
#                     dusts[i - 1][j - 1] += mount
#                     dusts[i + 1][j - 1] += mount
#                     count = 4
#                 map[i][j] == map[i][j] - mount * count  # 해당 구역 현재 확산량


def spread() :
    p = []
    for i in range(r):
        for j in range(c):
            if A[i][j] > 0 :
                s_dust = A[i][j] // 5
                cnt = 0
                for a in range(4):
                    ni = i + di[a]
                    nj = j + dj[a]
                    if 0 <= ni < r and 0 <= nj < c and A[ni][nj] != -1:
                        p.append((ni, nj, s_dust))
                        cnt += 1
                p.append((i, j , A[i][j] - (s_dust * cnt)))
                A[i][j] = 0

    for i, j, dust in p:
        A[i][j] += dust


def move() :
    A[machine[0][0]].insert(1,0)
    tmp = A[machine[0][0]].pop()
    for i in range(machine[0][0]-1, -1, -1):
        tmp, A[i][-1] = A[i][-1] , tmp
    A[0].insert(-1,tmp)
    for i in range(1, machine[0][0]):
        tmp, A[i][0] = A[i][0], tmp
    A[machine[1][0]].insert(1,0)
    tmp = A[machine[1][0]].pop()
    for i in range(machine[1][0]+1 , r):
        tmp, A[i][-1] = A[i][-1], tmp
    A[r-1].insert(-1,tmp)
    tmp = A[r-1].pop(0)
    for i in range(r-2, machine[1][0], -1):
        tmp, A[i][0] = A[i][0], tmp


def sum() :
    d = 0
    for i in range(r):
        for j in range(c):
            if A[i][j] > 0 :
                d += A[i][j]
    return d


if __name__ == '__main__' :
    # 입력
    r, c, t = map(int, input().split())

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    A = []
    machine = []

    for i in range(r):
        data = list(map(int, input().split()))
        A.append(data)
        for j in range(c):
            if data[j] == -1:
                machine.append((i,j)) #청소기 좌표 저장

    for _ in range(t):
        spread()
        move()

    print(sum())