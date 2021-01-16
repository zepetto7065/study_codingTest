# coding=utf-8

def solution(n) :
    answer = ""

    for i in range(n) :
        if i % 2 == 0 :
            text = "수"
        else :
            text = "박"
        answer += text

    return answer

print(solution(5))
