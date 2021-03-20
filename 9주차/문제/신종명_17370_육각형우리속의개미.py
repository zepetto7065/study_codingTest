n = int(input())

total_count = 0
map = [[0] * 100 for _ in range(100)]

dx = [[0, -1, 1], [0, -1, 1]]
dy = [[-1, 1, 1], [1, -1, -1]]

def dfs(x, y, type, count, bx, by):
    global total_count

    map[x][y] = 1

    if count > n:
        map[x][y] = 0
        return

    for i in range(3):
        nx = x + dx[int(type)][i]
        ny = y + dy[int(type)][i]

        if nx == bx and ny == by:
            continue

        if map[nx][ny] == 1:
            if count == n:
                # print(total_count)
                total_count += 1
        else:
            dfs(nx, ny, not type, count + 1, x, y)

    map[x][y] = 0


dfs(50, 50, 0, 0, 50, 50)

print(int(total_count / 3))
