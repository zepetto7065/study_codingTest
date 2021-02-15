import itertools

numbers = "011"


# 소수 판별한다.
def prime(n) :
    if n <= 1 :
        return False
    for num in range(2, n) :
        if n % num == 0 :
            return False
    return True


# 숫자를 만든다
def solution(numbers) :
    answer = 0
    s = set() #중복을 허락하지 않는다
    for i in range(len(numbers), 0, -1) :
        for n in list(map("".join, itertools.permutations(numbers, i))) :
            if prime(int(n)) is True :
                s.add(int(n))

    return len(s)


print(getNumber(numbers))
