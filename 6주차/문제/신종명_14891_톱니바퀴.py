from collections import deque

gears = [deque(map(int, input())) for _ in range(4)]
k = int(input())
inputs = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    num, direction = inputs[i]
    num -= 1

    right = gears[num][2]
    left = gears[num][6]
    gears[num].rotate(direction)
    tmp_direction = direction

    for j in range(num - 1, -1, -1):
        if gears[j][2] != left:
            left = gears[j][6]
            gears[j].rotate(direction * -1)
            direction *= -1
        else:
            break

    direction = tmp_direction
    for j in range(num + 1, 4):
        if gears[j][6] != right:
            right = gears[j][2]
            gears[j].rotate(direction * -1)
            direction *= -1
        else:
            break

result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2**i

print(result)
