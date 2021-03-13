import sys

n = int(input())
map = [list(map(int, list(input().split()))) for _ in range(n)]

minAns = sys.maxsize

for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x < x + d1 + d2 < n and d1 < y < y + d2 < n:
                    section = [[5 for _ in range(n)] for _ in range(n)]
                    # 1번 구역 설정
                    for i in range(d1 + 1):
                        r1, c1 = x + i, y - i
                        for tr in range(r1):
                            section[tr][c1] = 1

                    r2, c2 = x + d1, y - d1
                    for tc in range(c2):
                        for tr in range(r2):
                            section[tr][tc] = 1

                    # 2번 구역 설정
                    for i in range(d2 + 1):
                        r1, c1 = x + i, y + i
                        for tc in range(c1 + 1, n):
                            section[r1][tc] = 2

                    r2, c2 = x, y
                    for tr in range(r2):
                        for tc in range(c2 + 1, n):
                            section[tr][tc] = 2

                    # 3번 구역 설정
                    for i in range(d2 + 1):
                        r1, c1 = x + d1 + i, y - d1 + i
                        for tc in range(c1):
                            section[r1][tc] = 3

                    r2, c2 = x + d1 + d2, y - d1 + d2
                    for tr in range(r2 + 1, n):
                        for tc in range(c2):
                            section[tr][tc] = 3

                    # 4번 구역 설정
                    for i in range(d1 + 1):
                        r1, c1 = x + d2 + i, y + d2 - i
                        for tr in range(r1 + 1, n):
                            section[tr][c1] = 4

                    r2, c2 = x + d2, y + d2
                    for tc in range(c2 + 1, n):
                        for tr in range(r2 + 1, n):
                            section[tr][tc] = 4

                    cal = [0 for _ in range(6)]

                    for r in range(n):
                        for c in range(n):
                            sec = section[r][c]
                            cal[sec] += map[r][c]

                    ans = max(cal[1:]) - min(cal[1:])
                    if minAns > ans:
                        minAns = ans

print(minAns)
