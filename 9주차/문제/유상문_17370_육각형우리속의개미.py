import sys

chk = [False] * 2001
weight = [23,1,1,-23,-1,-1]
N = int(sys.stdin.readline())

def calc(cnt, cur, w) :
    if cnt == 0:
        if chk[cur]:
            return 1
        else:
            return 0
    if chk[cur]:
        return 0

    chk[cur] = True
    temp = calc(cnt - 1, cur + weight[(w + 5) % 6], (w + 5) % 6) + calc(cnt -1 , cur + weight[(w + 1) % 6], (w + 1) % 6)
    chk[cur] = False

    return temp


chk[1000] = True

print(calc(N, 1000 + weight[0] , 0))