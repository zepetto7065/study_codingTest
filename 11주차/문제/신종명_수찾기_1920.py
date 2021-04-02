import sys


def binary_search(list, target, left, right):
    while left <= right:
        mid_index = (left + right) // 2
        if list[mid_index] == target:
            return True
        elif list[mid_index] < target:
            left = mid_index + 1
        else:
            right = mid_index - 1
    return False


n = int(sys.stdin.readline())
target_numbers = list(map(int, sys.stdin.readline().split()))
target_numbers.sort()

m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
for number in numbers:
    if binary_search(target_numbers, number, 0, n - 1):
        print(1)
    else:
        print(0)
