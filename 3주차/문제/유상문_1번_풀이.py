# https://programmers.co.kr/learn/courses/30/lessons/42862 체육복

# n = 5
# lost = [2,4] # x
# reserve = [3] # 2
# n = 5
# lost = [2, 4]
# reserve = [3]
n = 5
lost = [1,3,5]
reserve = [2,3]
# n = 5
# lost = [1,2,3,4,5]
# reserve = [2,4]


def solution(n, lost, reserve):
    list = []
    answer = 0
    # 번호순으로 옷 개수 지정
    for i in range(1, n+1):
        if i in lost and i in reserve:
            list.append(1)
        elif i in lost :
            list.append(0)
        elif i in reserve :
            list.append(2)
        else:
            list.append(1)

    # 조건에 따른 옷 분류
    for j in range(n):
        if list[j] == 2 :
            if j > 0 and list[j-1] == 0:
                list[j-1] = 1
                list[j] = 1
            elif j < n-1 and list[j+1] == 0:
                list[j+1] = 1
                list[j] = 1

    for clothe in list:
        if clothe >= 1 :
            answer += 1


    return answer

print(solution(n,lost,reserve))