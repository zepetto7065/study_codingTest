def solution(name):
    arr = list(map(lambda x : ord(x)-65 if x<"N" else 91-ord(x), name))

    length = len(arr)
    answer = sum(arr)
    idx = 0
    goRight = True
    arr[idx] = 0

    while (sum(arr)!=0):
        
        right, left = 1, 1
        while (arr[idx + right]==0):
            right+=1
        while (arr[idx - left]==0):
            left+=1
        if right> left:
            idx -=1
            goRight = False
        elif right < left:
            idx +=1
            goRight = True
        else:
            if goRight:
                idx +=1
            else:
                idx -=1
        answer += 1
        arr[idx] = 0

        
    return answer