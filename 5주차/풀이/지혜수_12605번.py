n = int(input())

for i in range(n):
  print("Case #",i+1,": "," ".join(input().split()[::-1]), sep="")