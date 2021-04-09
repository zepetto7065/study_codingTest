from bisect import bisect_left

N = int(input())

arr = sorted(list(map(int, input().split())))

M = int(input())

tmp = list(map(int, input().split()))

for i in range(M):
    idx1 = bisect_left(arr, tmp[i])
    if idx1 >= len(arr) or arr[idx1] != tmp[i]:
        print(0, end=" ")
    else:
        idx2 = bisect_left(arr, tmp[i] + 1)
        print(idx2 - idx1, end=" ")
