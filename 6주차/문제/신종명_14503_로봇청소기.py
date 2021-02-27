n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(direction):
    return (direction + 3) % 4


count = 1
board[x][y] = 2

while True:
    check = False
    for i in range(4):
        nd = rotate(d)
        next_x = x + dx[nd]
        next_y = y + dy[nd]
        d = nd

        if not board[next_x][next_y]:
            board[next_x][next_y] = 2
            count += 1
            x = next_x
            y = next_y
            check = True
            break

    if not check:
        if board[x - dx[d]][y - dy[d]] == 1:
            print(count)
            break
        else:
            x = x - dx[d]
            y = y - dy[d]
