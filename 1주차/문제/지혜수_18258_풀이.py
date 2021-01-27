import sys
from collections import deque

queue = deque()

def push(input):
    queue.append(input)

def empty():
    print(1 if size() == 0 else 0) 

def pop():
    try:
        print(queue.popleft())
    except:
        print('-1')

def size():
    return len(queue)

def front():
    print(queue[0] if size() != 0 else -1)

def back():
    print(queue[-1] if size()!=0 else -1)
        
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        push(cmd[1])

    elif cmd[0] == 'pop':
        pop()

    elif cmd[0] == 'empty':
        empty()

    elif cmd[0] == 'size':
        print(size())

    elif cmd[0] == 'front':
        front()

    elif cmd[0] == 'back':
        back()