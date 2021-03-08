if __name__ == '__main__' :
    num = list(map(int, input().split()))
    sortedNum = sorted(num)

    while True :
        for i in range(len(num)-1):
            if num[i] > num[i+1] :
                num[i], num[i + 1] = num[i + 1], num[i]
                print(" ".join(map(str, num)))

        if num == sortedNum :
            break

