def solution(number, k):
    l = len(number)-k
    tmp = "0"
    idx = 0
    for i, x in enumerate(number[:k+1]):
        if tmp < x:
            idx, tmp = i, x
    k -= idx
    answer=number[idx:]

    idx = 0
    while(k != 0 and len(answer) != l):
        if answer[idx]<answer[idx+1]:
            answer=answer[:idx]+answer[idx+1:]
            k-=1
            idx -=1
        else:
            idx+=1
        if idx +1 == len(answer):
            answer=answer[:l]
    return answer