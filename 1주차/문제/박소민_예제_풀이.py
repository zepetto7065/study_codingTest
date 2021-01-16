def solution(n):
    answer = ''
    a = '수'
    b = '박'
    answer = a
    for _ in range(n):
        if answer[-1] == a:
            answer += b
        else:
            answer += a
    answer = answer[:n]
    return answer


print(solution(3))
print(solution(4))
