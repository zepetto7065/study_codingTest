N, M = map(int, input().split())
d = {}
for n in range(N):
  tmp = input().split()
  d[tmp[0]] = tmp[1]
for m in range(M):
  print(d[input()])