import sys

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) > 0 :
        return stack.pop()
    else:
        return '-1'

def size():
    return len(stack)

def empty():
    if len(stack) > 0:
        return '0'
    else:
        return '1'
def top():
    if len(stack) > 0:
        return stack[-1]
    else :
        return '-1'

n = int(input())

for _ in range(n):
    #시간 초과로 인한 sys 내장 라이브러리 사용
    #띄어쓰기와 \n까지 포함하므로 split()을 이용하는 것이 좋다.
    #여러줄 입력 받고 싶다면 sys.stdin
    x = sys.stdin.readline()

    if 'push' in x:
        push(x.split()[1])
    elif 'pop' in x:
        print(pop())
    elif 'size' in x:
        print(size())
    elif 'empty' in x:
        print(empty())
    else:
        print(top())