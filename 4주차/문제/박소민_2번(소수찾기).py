from itertools import permutations


def solution(numbers):
    all_num = []
    answer = 0
    for i in range(len(numbers)):
        num = list(permutations(list(numbers), i+1))
        all_num += [int("".join(i))for i in num]
    for k in set(all_num):
        tmp = 0
        for i in range(1, k+1):
            if k % i == 0 and k != 0 and k != 1:
                tmp += 1
            if tmp >= 3:
                break
        if tmp == 2:
            answer += 1
    return answer
