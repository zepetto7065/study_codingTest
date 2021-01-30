import sys

def solution(c):
    a={}
    b=1
    for x, y in c:
        if y in a:
            a[y]+=1
        else:
            a[y]=1
    for x in a.values():
        b*=(x+1)
    print(b-1)

n = int(sys.stdin.readline())
for x in range(n):
    k = int(sys.stdin.readline())
    tmp = []
    for y in range(k):
        tmp.append(sys.stdin.readline().split())
    solution(tmp)