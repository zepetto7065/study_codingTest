from itertools import combinations


def solution(number, k):
    stack = []

    for (i, num) in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break;

        stack.append(num)

    #남아있는 k
    if k > 0 : stack = stack[:-k]
    answer = "".join(stack)
    return answer



# print(solution("1924",2))
# print(solution("1231234",3))
# print(solution("1249541", 2))
print(solution("4177252841",4))
print('hello')
