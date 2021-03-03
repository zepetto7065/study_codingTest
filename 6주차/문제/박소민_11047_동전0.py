n, k = map(int, input().split(' '))
money = []
value = 0
for _ in range(n):
    a = int(input())
    money.append(a)
    money.sort(reverse=True)
for i in range(0, n):
    coin = money[i]
    if k >= coin:
        num = k//coin
        k -= coin*num
        value += num
    else:
        continue
print(value)
