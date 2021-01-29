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
    return b-1