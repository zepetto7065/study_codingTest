dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r, c, t = map(int, input().split(' '))
room = [list(map(int, input().split(' '))) for _ in range(r)]

location = (0, 0)
for i in range(r):
    if room[i][0] == -1 and room[i + 1][0] == -1:
        location = (i, i + 1)
        break

for _ in range(t):
    dusty_room = [[0] * c for _ in range(r)]

    for i in range(0, r):
        for j in range(0, c):
            if room[i][j] >= 5:
                cnt = 0
                for k in range(0, 4):
                    ai = i + dx[k]
                    aj = j + dy[k]
                    if 0 <= ai < r and 0 <= aj < c and room[ai][aj] != -1:
                        cnt += 1
                        dusty_room[ai][aj] += room[i][j] // 5
                room[i][j] = room[i][j] - room[i][j] // 5 * cnt

    for i in range(r):
        for j in range(c):
            room[i][j] += dusty_room[i][j]

    x = location[0]
    y = location[1]

    value1 = room[x][-1]
    value2 = room[0][-1]
    value3 = room[0][0]

    for i in range(c - 2, 0, -1):
        room[x][i + 1] = room[x][i]
    for i in range(1, x):
        room[i - 1][-1] = room[i][-1]
    for i in range(1, c):
        room[0][i - 1] = room[0][i]
    for i in range(x - 2, -1, -1):
        if room[i + 1][0] == -1:
            break
        room[i + 1][0] = room[i][0]

    room[x][1] = 0
    room[x - 1][-1] = value1
    room[0][-2] = value2
    room[1][0] = value3

    value1 = room[y][-1]
    value2 = room[-1][-1]
    value3 = room[-1][0]

    for i in range(c - 2, 0, -1):
        room[y][i + 1] = room[y][i]
    for i in range(r - 2, y - 1, -1):
        room[i + 1][-1] = room[i][-1]
    for i in range(1, c):
        room[-1][i - 1] = room[-1][i]
    for i in range(y + 2, r):
        if room[i - 1][0] == -1:
            break
        room[i - 1][0] = room[i][0]

    room[y][1] = 0
    room[y + 1][-1] = value1
    room[-1][-2] = value2
    room[-2][0] = value3

all_value = 0
for value in room:
    all_value += sum(value)

print(all_value + 2)

