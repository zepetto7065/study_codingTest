# 재귀
a = int(input())


def f_sum(n):
    if n <= 1:
        return n

    else:
        value = f_sum(n-1)+f_sum(n-2)
        return value


print(f_sum(a))

#
n = int(input())
fibo = []
for i in range(n + 1):
    if i <= 1:
        fibo.append(i)
        continue
    fibo.append(fibo[i - 1] + fibo[i - 2])
print(fibo[n])
