a = []
result = []
cnt = 0
no = ''
n = int(input())
for _ in range(n):
    x = int(input())
    while cnt < x:
        cnt += 1
        a.append(cnt)
        result.append("+")
    if a[-1] == x and len(a) > 0:
        a.pop()
        result.append("-")
    else:
        no = 'NO'
        break
if no == 'NO':
    for _ in result:
        print(_)
else:
    print(result)
