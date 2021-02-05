import collections

name = "KAATSV" #01234



def solution(name):
    answer = 0

    #이름의 길이 구한다
    name_list = list(name)
    for i in range(0,len(name_list) // 2):
        if ( ('A' == name_list[i - 1] or 'A' == name_list[i + 1]) and 'A' == name[i] ) is True :
            name_list.remove('A')

    temp = name_list[len(name_list)//2 - 1 : len(name_list)]
    temp.reverse()

    result = collections.Counter(name_list) - collections.Counter(temp)
    order = list(result)
    for char in temp:
        order.append(char)

    #이름의 길이만큼 반복문
    for char in order:
        # 이하 숫자 이동
        # a는 97 , b는 98... ASCII code 변환 M,N이 중간
        # M보다 작으면 올리고 N보다 크면 내리고
        if 65 < ord(char) <= 77 :
            answer += ord(char) - 65
        elif ord(char) > 77 :
            answer += 90 - ord(char) + 1
        elif ord(char) == 65 :
            continue
        answer += name_list.index(char)

    return answer - 1

print(solution(name))