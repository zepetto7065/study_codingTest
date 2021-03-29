import sys

n = int(sys.stdin.readline())
N = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))


def binary(check, list) :
    list_len = len(list)

    if (list_len == 0) :
        return print('0')

    mid = list_len // 2

    if (list[mid] == check) :
        return print('1')
    elif (list[mid] > check) :
        return binary(check, list[:mid])
    else :
        return binary(check, list[mid + 1 :])


for check in M :
    binary(check, N)

# 그냥 search
# for i in range(M):
#     if second[i] in first:
#         print(1)
#     else:
#         print(0)
