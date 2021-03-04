n = int(input())

count = 1
while True:
    if n == 1:
        print(count)
        break

    if n % 2 == 0:
        n /= 2
    else:
        n = (3 * n) + 1

    count += 1
