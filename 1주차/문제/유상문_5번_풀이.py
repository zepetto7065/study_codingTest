n = int(input())
stack  = []
result = []

no_yn = False;
count = 0

for i in range(n):
    c = int(input())

    while count < c:
        count+=1
        stack.append(count)
        result.append("+")

    if stack[-1] == c:
        stack.pop()
        result.append("-")
    else:
        no_yn = True
        break

if no_yn is True:
    print("NO")
else:
    for i in result:
        print(i)