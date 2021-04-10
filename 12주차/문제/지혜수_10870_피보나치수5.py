def fibo(n):
  a = 0
  b = 1
  c = 0
  for _ in range(n-1):
    c = a + b
    a, b = b, c
  return c

N = int(input())
if N == 0:
  print(0)
elif N == 1:
  print(1)
else:
  print(fibo(N))