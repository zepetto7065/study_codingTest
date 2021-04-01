
# n, c = map(int, input().split(' '))
# house = []
# for _ in range(n):
#     x = int(input())
#     house.append(x)
# house.sort()


# left = 0
# right = len(house)-1
# mid = 1
# a = house[mid] - house[left]
# b = house[right] - house[mid]

# for i in range(1, len(house)//2):
#     y = min(a, b)
#     if min(house[mid+i]-house[left], house[right]-house[mid+1]) > y:
#         a = house[mid+i]-house[left]
#         b = house[right]-house[mid+i]

# print(min(a, b))
n, c = map(int, input().split(' '))

arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

low = arr[1] - arr[0]
high = arr[-1] - arr[0]
result = 0

while(low <= high):
    mid = (low + high) // 2

    value = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우 =>간격 늘리기
        low = mid + 1
        result = mid
    else:  # c개 이상의 공유기를 설치할 수 없는 경우 =>간격이 너무 넓은것! 간격 좁히기
        high = mid - 1

print(result)
