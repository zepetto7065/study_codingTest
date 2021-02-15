def solution(answers):
    a =0
    b =0
    c =0
    aa = [1,2,3,4,5]*len(answers)
    bb = [2,1,2,3,2,4,2,5]*len(answers)
    cc = [3,3,1,1,2,2,4,4,5,5]*len(answers)
    for x in range(len(answers)):
        if answers[x] == aa[x]:
            a+=1
        if answers[x] == bb[x]:
            b+=1
        if answers[x] == cc[x]:
            c+=1

    k = sorted({1:a,2:b,3:c}.items(), key=(lambda x:x[1]), reverse = True)

    if k[0][1] == k[2][1]:
        return [1,2,3]
    elif k[0][1] == k[1][1]:
        return[k[0][0],k[1][0]]
    else:
        return[k[0][0]]