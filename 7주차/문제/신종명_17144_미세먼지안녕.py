r, c, t = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(r)]


def spread():
    temp = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if house[x][y] >= 5:
                amount = house[x][y] // 5

                if amount == 0:
                    return

                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < r and 0 <= ny < c and house[nx][ny] != -1:
                        temp[nx][ny] += amount
                        house[x][y] -= amount

    for i in range(r):
        for j in range(c):
            house[i][j] += temp[i][j]


def find_air_cleaner_location():
    for i in range(r):
        if house[i][0] == -1:
            return i


def purify(location):
    top = location
    bottom = location + 1

    for i in range(top - 1, 0, -1):
        house[i][0] = house[i - 1][0]

    for i in range(0, c - 1):
        house[0][i] = house[0][i + 1]

    for i in range(0, top):
        house[i][c - 1] = house[i + 1][c - 1]

    for i in range(c - 1, 1, -1):
        house[top][i] = house[top][i - 1]
    house[top][1] = 0

    for i in range(bottom + 1, r - 1):
        house[i][0] = house[i + 1][0]

    for i in range(0, c - 1):
        house[r - 1][i] = house[r - 1][i + 1]

    for i in range(r - 1, bottom, -1):
        house[i][c - 1] = house[i - 1][c - 1]

    for i in range(c - 1, 1, -1):
        house[bottom][i] = house[bottom][i - 1]
    house[bottom][1] = 0


for _ in range(t):
    spread()
    air_cleaner_location = find_air_cleaner_location()
    purify(air_cleaner_location)

total = sum(list(filter(lambda x: x > 0, sum(house, []))))
print(total)
