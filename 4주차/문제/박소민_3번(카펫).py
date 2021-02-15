# 정답 = yellow의 가로길이+2,yellow의 세로길이+2
# 가로길이,세로길이 모두 yellow의 약수
# brown의 개수 = yellow가로길이*2+yellow세로길이*2 +4(모서리)
# brown의 개수랑 맞으면 answer에 append해서 return


def solution(brown, yellow):
    answer = []

    y_x, y_y = 0, 0

    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_x = int(yellow / i)
            y_y = i
            if (y_x*2) + (y_y*2) + 4 == brown:
                answer.append(y_x + 2)
                answer.append(y_y + 2)
                break

    return answer
