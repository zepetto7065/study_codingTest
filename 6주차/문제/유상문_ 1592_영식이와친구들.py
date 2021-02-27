import sys

n, m, l = map(int,sys.stdin.readline().split())

def solution(n,m,l):
    member = [0]*n
    i = 0
    count = 0
    while True:
        member[i] += 1
        if member[i] == m:
            print(count)
            break
        i = (i + l)%n
        count += 1


solution(n,m,l)
