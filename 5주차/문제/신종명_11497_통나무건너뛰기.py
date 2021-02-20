count = int(input())

for _ in range(count):
    n = int(input())
    heights = list(map(int, input().split()))
    heights.sort()

    result = max(map(lambda i: heights[i] - heights[i - 2], range(2, n)))

    print(result)
