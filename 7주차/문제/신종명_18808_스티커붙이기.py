n, m, k = map(int, input().split())

laptop = [[0] * m for _ in range(n)]


def isAttachable(a, b, sticker):
    if len(sticker) + a > n or len(sticker[0]) + b > m:
        return False

    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if x + a < n and y + b < m:
                if sticker[x][y] == 1 and laptop[x + a][y + b] == 1:
                    return False
            else:
                break

    return True


def attach(x, y, sticker):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                laptop[i + x][j + y] = 1

def tryToAttach(sticker):
    for i in range(n):
        for j in range(m):
            if isAttachable(i, j, sticker):
                attach(i, j, sticker)
                return True
    return False


def rotate(sticker):
    x = len(sticker)
    y = len(sticker[0])

    rotated_sticker = [[sticker[x - j - 1][i] for j in range(x)] for i in range(y)]

    return rotated_sticker


for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]

    for _ in range(4):
        if tryToAttach(sticker) is True:
            break

        sticker = rotate(sticker)

count = 0
for i in range(n):
    for j in range(m):
        if laptop[i][j] == 1:
            count += 1
print(count)
