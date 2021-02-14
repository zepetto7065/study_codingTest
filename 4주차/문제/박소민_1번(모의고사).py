def solution(answers):
    answer = []
    one_count = 0
    two_count = 0
    three_count = 0
    list_one = [1, 2, 3, 4, 5] * 2000
    list_two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    list_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    for i in range(len(answers)):
        if list_one[i] == answers[i]:
            one_count += 1
        if list_two[i] == answers[i]:
            two_count += 1
        if list_three[i] == answers[i]:
            three_count += 1

    max_num = max(one_count, two_count, three_count)
    if max_num == one_count:
        answer.append(1)
    if max_num == two_count:
        answer.append(2)
    if max_num == three_count:
        answer.append(3)
    answer.sort()
    return answer
