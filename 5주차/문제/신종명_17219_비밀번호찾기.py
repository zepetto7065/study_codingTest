n, m = map(int, input().split())
dic = {}

for _ in range(n):
    homepage, password = input().split()
    dic[homepage] = password

for _ in range(m):
    print(dic[input()])
