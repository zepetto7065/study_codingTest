
n = int(input())
stack = []

for i in range(1,n+1):
    stack.append(i)

temp = []

for i in range(1, n+1):
    c = int(input())
    if len(stack):
        if i == 1 :
            for j in range(1,c+1):
                temp.append(j)
                stack.remove(j)
                print('+')
            temp.pop()
            print('-')
        elif c == temp[-1]:
            temp.pop()
            print('-')
        else:
            for k in range(stack[0], c+1):
                temp.append(k)
                stack.remove(k)
                print('+')
            temp.pop()
            print('-')
    else:
        for _ in range(len(stack)):
            print('-')









