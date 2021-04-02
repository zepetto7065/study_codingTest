# import sys
#
# n = int(sys.stdin.readline())
#
# numbers = list(map(int, sys.stdin.readline().split()))
#
# dp = [1 for i in range(n)]
#
# for i in range(1, n):
#     for j in range(i):
#         if numbers[i] > numbers[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))

import sys


def lower_bound(left, right, number):
    while left < right:
        mid = (left + right) // 2

        if answers[mid] < number:
            left = mid + 1
        else:
            right = mid
    return right


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

answers = []

for number in numbers:
    if len(answers) == 0:
        answers.append(number)
        continue

    if answers[-1] < number:
        answers.append(number)
    else:
        index = lower_bound(0, len(answers) - 1, number)
        answers[index] = number

print(len(answers))
