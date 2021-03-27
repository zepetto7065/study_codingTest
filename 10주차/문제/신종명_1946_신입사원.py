import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    result = [list(map(int, input().split())) for _ in range(n)]
    result.sort(key=lambda x: x[0])

    count = 1
    grade = result[0][1]
    for i in range(1, n):
        grade = min(grade, result[i][1])
        if grade == result[i][1]:
            count += 1

    print(count)
