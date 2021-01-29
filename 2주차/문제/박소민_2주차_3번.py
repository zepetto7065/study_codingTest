def solution(clothes):
    answer = 1
    result = {}
    for i in range(len(clothes)):
        name = clothes[i][1]
        value = clothes[i][0]
        if name in result:
            result[name].append(value)
        else:
            result[name] = [value]
    for key in result.keys():
        answer *= len(result[key]) + 1

    return answer-1
