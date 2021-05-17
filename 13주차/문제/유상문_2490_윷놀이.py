examList = []

# 입력
for i in range(3) :
    examList.append(list(map(int, input().split())))

# 출력
for i in range(3) :
    count = 0
    for j in range(4) :
        if examList[i][j] == 1 :
            count += 1
    if count == 0 :
        # 윷
        print('D')
    elif count == 1 :
        # 걸
        print('C')
    elif count == 2 :
        # 개
        print('B')
    elif count == 3 :
        # 도
        print('A')
    else :
        # 모
        print('E')

