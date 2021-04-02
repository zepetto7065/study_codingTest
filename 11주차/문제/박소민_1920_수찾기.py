import sys
sys.stdin = open("input.txt", "r")

n = int(input())
alist = list(map(int, input().split(' ')))
m = int(input())
alist.sort()
mm = list(map(int, input().split(' ')))
for x in mm:
    left = 0
    right = len(alist)-1

    while left <= right:
        mid = (left+right)//2
        if alist[mid] == x:
            print(1)
            break
        elif alist[mid] > x:
            right = mid-1
        else:
            left = mid+1
    else:
        print(0)

# 역시 이 방법은 안되는군요!
# for x in mm:
#     if x in alist:
#         print(1)
#     else:
#         print(0)
