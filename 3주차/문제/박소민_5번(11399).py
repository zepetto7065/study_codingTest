n = int(input())
Atmlist = list(map(int, input().split()))
Atmlist.sort()
minSum = 0
a = 0
for i in range(n):
    minSum += (a+Atmlist[i])
    a += Atmlist[i]

print(minSum)
