def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)

    for i in reserve:
        if i in lost:
            lost.remove(i)
        elif (i-1) in lost:
            lost.remove(i-1)
        elif i+1 in lost and i+1 not in reserve:
            lost.remove(i+1)

    return n - len(lost)