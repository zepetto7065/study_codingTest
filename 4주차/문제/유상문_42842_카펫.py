brown=24
yellow=24

def solution(brown, yellow):
    answer = []
    divisor = []
    #약수를 구한다
    for i in range(1, yellow+1):
        if yellow % i == 0:
           divisor.append(i)

    #짝수개로 맞춘다
    if len(divisor)//2 :
        divisor.insert(len(divisor)//2, divisor[len(divisor)//2])

    #규칙에 의해 정답 도출
    for j in range(len(divisor)):
        a = divisor[j]
        b = divisor[len(divisor) - j -1]
        if (a+b+2) * 2 == brown:
            answer = [a+2, b+2]
    return answer
print(solution(brown,yellow))