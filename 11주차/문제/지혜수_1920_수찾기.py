N = input()

arr = sorted(list(map(int, input().split())))

M = int(input())

def search(nums, target):
  left, right = 0, len(nums)-1
  while left <= right:
    mid = (left + right)// 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    else:
      return 1
  return 0

tmp = list(map(int, input().split()))

for x in tmp:
  print(search(arr, x))