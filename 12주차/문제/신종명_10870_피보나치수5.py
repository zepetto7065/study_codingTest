n = int(input())

fibo = []

for i in range(n + 1):
    if i <= 1:
        fibo.append(i)
        continue

    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[n])
