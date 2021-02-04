from itertools import combinations


def solution(number, k) :
    answer = ''
    numbers = list(number)
    l = len(numbers) - k

    index = 0
    slice = k

    for i in range(l):
        slice_numbers = numbers[index :index + slice]

        if len(slice_numbers) >= slice:

            max_num = max(slice_numbers)
            index += numbers.index(max_num) + 1
            slice -= 1
            answer += max_num
        else:
            answer += numbers[len(numbers)-1]
    return answer

# print(solution("1924",2))
print(solution("1231234",3))
# print(solution("4177252841",4))
print('hello')