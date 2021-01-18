stack = []
n = int(input())

for _ in range(n) :
    x = int(input())

    if x != 0 :
        stack.append(x)
    else :
        stack.pop()


def add(length) :
    sum = 0
    for i in range(length) :
        sum += stack[i]
    return sum


print(add(len(stack)))
