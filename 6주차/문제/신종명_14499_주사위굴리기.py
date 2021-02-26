n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]
temp = [0, 0, 0, 0, 0, 0]

direction = [
    [2, 0, 5, 3, 4, 1],  # 동쪽
    [1, 5, 0, 3, 4, 2],  # 서쪽
    [4, 1, 2, 0, 5, 3],  # 북쪽
    [3, 1, 2, 5, 0, 4]  # 남쪽
]

for command in commands:
    command -= 1
    x = x + dx[command]
    y = y + dy[command]

    if x < 0 or x >= n or y < 0 or y >= m:
        x = x - dx[command]
        y = y - dy[command]
        continue

    for idx in range(6):
        temp[idx] = dice[idx]

    for idx in range(6):
        dice[idx] = temp[direction[command][idx]]

    if board[x][y]:
        dice[5] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[5]

    print(dice[0])
