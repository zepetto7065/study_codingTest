from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    for i in range(1,len(numbers)+1):
        arr.extend(map(lambda x :int(''.join(x)), list(permutations(numbers,i))))
    arr=set(arr)
    for x in arr:
        tag = True
        if x != 0 and x != 1:
            for t in range(2, (x//2+1)):
                if x % t == 0:
                    tag = False
                    break
            if tag == True:
                answer += 1
    return answer