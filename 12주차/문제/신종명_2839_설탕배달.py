n = int(input())

dp = [-1] * (n + 1)

for i in range(n + 1):
    if i - 3 < 0:
        continue

    if i == 3:
        dp[i] = 1
        continue

    if i == 5:
        dp[i] = 1
        continue

    if i - 5 < 0 and dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1
        continue

    if dp[i - 3] != -1 and dp[i - 5] != -1:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    elif dp[i - 5] != -1:
        dp[i] = dp[i - 5] + 1
    elif dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1

print(dp[n])

# count = 0
# while True:
#     if n < 0:
#         count = -1
#         break
#
#     if n == 0:
#         break
#
#     if n % 5 == 0:
#         count += n // 5
#         break
#
#     n -= 3
#     count += 1
#
# print(count)
