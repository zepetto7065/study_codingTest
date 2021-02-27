n, m, l = map(int, input().split())

friends = [0] * n
index = 0
count = 0

while True:
    friends[index] += 1

    if friends[index] == m:
        print(count)
        break

    if friends[index] % 2 == 0:
        index = (index - l) % n
    else:
        index = (index + l) % n

    count += 1
