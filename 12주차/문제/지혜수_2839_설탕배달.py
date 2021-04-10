n = int(input())
k = -1
for x in range(n//5,-1,-1):
    if (n-5*x) % 3 == 0:
        k = x  + (n-5*x) // 3
        break
print (k)