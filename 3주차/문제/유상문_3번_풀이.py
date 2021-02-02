from itertools import combinations


def solution(number, k):
    item = list("1924")
    temp = list(combinations(item, len(item) - 2))
    numbers = []
    for char in temp:
        num = ''
        for i in char:
            num += i
        numbers.append(int(num))

    numbers.sort()
    result = numbers[len(numbers)-1]

    return str(result)

print(solution(1234,2))
print('hello')