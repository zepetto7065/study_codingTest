from collections import deque
import sys

queue = deque()

def push(x):
    queue.append(x)
def pop():
    if len(queue) > 0 :
        return queue.popleft()
    else:
        return -1
def size():
    return len(queue)
def empty():
    if len(queue) > 0 :
        return 0
    else:
        return 1
def front():
    if len(queue) > 0 :
        return queue[0]
    else:
        return -1
def back():
    if len(queue) > 0:
        return queue[len(queue)-1]
    else:
        return -1


n = int(input())

for _ in range(n):
    command = sys.stdin.readline()
    if 'push' in command:
        push(command.split()[1])
    elif 'pop' in command:
        print(pop())
    elif 'size' in command :
        print(size())
    elif 'empty' in command:
        print(empty())
    elif 'front' in command:
        print(front())
    elif 'back' in command:
        print(back())