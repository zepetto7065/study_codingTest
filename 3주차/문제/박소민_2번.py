# 실패
def solution(name):
    answer = 0
    fristname = 'A'*len(name)
    a = 0
    for i, j in zip(fristname, name):
        i = ord(i)
        j = ord(j)
        if j == 'A':
            answer += 1
            continue
        else:
            a = min((j-65), (91-j))
            answer += a
            answer += 1
    return answer-1
