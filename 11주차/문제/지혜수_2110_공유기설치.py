N, C = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

answer = 0

start, end =  1, arr[-1] - arr[0]

while start <= end:
  mid = (start + end)// 2    
  # print('mid: ', mid)
  count = 1
  current = arr[0]

  for i in range(1,N):
    if arr[i] >= current + mid:
      count += 1
      current = arr[i]

  if count >= C:
    start = mid + 1
    answer = mid
    # print('start의 변화: ',start)
  else:
    end = mid - 1
    # print('end의 변화: ', end)
print(answer)
