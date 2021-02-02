from itertools import combinations


def solution(number, k):
    item = list("1924")
    temp = list(combinations(item, len(item) - 2))
    numbers = []
    for str in temp:
        num = ''
        for i in str:
            num += i
        numbers.append(int(num))

    numbers.sort()
    return ''.join(numbers.reverse())

print(solution(1234,2))