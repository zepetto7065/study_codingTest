import heapq
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maps = []
for _ in range(m) :
    maps.append(list(sys.stdin.readline()))
visited = [[0] * n for _ in range(m)]


def bfs(start, maps, visited) :
    dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    queue = []
    heapq.heappush(queue, start)

    while queue :
        cnt, y, x = heapq.heappop(queue)
        visited[y][x] = 1
        if y == m - 1 and x == n - 1 :
            return cnt

        for dy, dx in dirs :
            ny, nx = y + dy, x + dx
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] :
                visited[ny][nx] = 1
                if maps[ny][nx] == "0" :
                    heapq.heappush(queue, (cnt, ny, nx))
                elif maps[ny][nx] == "1" :
                    heapq.heappush(queue, (cnt + 1, ny, nx))



print(bfs((0, 0, 0), maps, visited))
