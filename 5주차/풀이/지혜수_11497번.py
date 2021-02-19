T = int(input())

for _ in range(T):
  n = input()
  arr = list(map(int, input().split()))
  arr = sorted(arr)
  
  print(max(list(map(lambda x: arr[x+2]-arr[x], range(len(arr)-2)))))