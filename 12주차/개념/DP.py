# 다이나믹 프로그래밍 (DP)

# 정의
# 특정 범위까지의 값을 구하기 위해서 그것과 다른 범위까지의 값을 이용하여 효율적으로 값을 구하는 알고리즘 설계 기법이다.

# 조건
# 1. Problem을 더 작은 Sub Problem으로 쪼갤 수 있을 경우
# 2. Sub Problem의 솔루션으로 더 큰 Problem의 솔루션을 구할 수 있을 경우
# 3. Sub Problem들이 겹칠 경우 (memorization으로 계산수를 줄일 수 있다.)

import time


def fib(n):
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)


array = []


def fib_top_down(n):
    if n < len(array):
        return array[n]
    else:
        next_value = n if n <= 1 else fib_top_down(n - 1) + fib_top_down(n - 2)
        array.append(next_value)
        return next_value


def fib_dp_bottom_up(n):
    fibo = []

    for i in range(n + 1):
        if i <= 1:
            fibo.append(i)
            continue

        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n]


start = time.time()
# call stack error
# print(fib(10000))
print(fib(30))
print(time.time() - start)

start = time.time()

print(fib_dp_bottom_up(20000))

print(time.time() - start)

start = time.time()

print(fib_top_down(800))

print(time.time() - start)
