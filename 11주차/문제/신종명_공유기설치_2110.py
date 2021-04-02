import sys

n, c = map(int, sys.stdin.readline().split())

house = [int(sys.stdin.readline()) for _ in range(n)]
house.sort()

min_distance = 1
max_distance = house[-1] - house[0]
answer = 0
while min_distance <= max_distance:
    mid = (min_distance + max_distance) // 2

    wifi_count = 1
    before_house = house[0]
    for i in range(1, n):
        if house[i] >= before_house + mid:
            wifi_count += 1
            before_house = house[i]

    if wifi_count < c:
        max_distance = mid - 1
    else:
        min_distance = mid + 1
        answer = mid

print(answer)
