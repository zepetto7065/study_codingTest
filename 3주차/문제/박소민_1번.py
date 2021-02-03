def solution(n, lost, reserve):
    answer = n - len(lost)
    anotherLost = []

    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            answer += 1
        else:
            anotherLost.append(lost[i])

    for i in range(len(anotherLost)):
        if anotherLost[i]-1 in reserve:
            reserve.remove(anotherLost[i]-1)
            answer += 1
        elif anotherLost[i]+1 in reserve:
            reserve.remove(anotherLost[i]+1)
            answer += 1

        if len(reserve) == 0:
            break

    return answer
