import sys

n = int(sys.stdin.readline())
arr = list(range(n,0,-1))
answer = []
stack = []
x=0
try:
  while x != n:
    if len(stack) == 0:
      stack.append(arr.pop())
      answer.append('+')
    else:
      k = int(sys.stdin.readline())
      while k != stack[-1]:
        stack.append(arr.pop())
        answer.append('+')
      stack.pop()
      answer.append('-')
      x += 1
  for ans in answer:
    print(ans)
except:
  print('NO')