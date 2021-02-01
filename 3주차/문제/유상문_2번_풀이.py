name = "AA A SV" #01234



def solution(name):
    answer = 0
    move = 0
    #이름의 길이 구한다
    name_list = list(name)

    #이름의 길이만큼 반복문
    for char in name_list:

        answer += name_list.index(char)
        # 이하 숫자 이동
        # a는 97 , b는 98... ASCII code 변환 M,N이 중간
        # M보다 작으면 올리고 N보다 크면 내리고
        if 65 < ord(char) <= 77 :
            answer += ord(char) - 65
        elif ord(char) > 77 :
            answer += 90 - ord(char) + 1
        elif ord(char) == 65 :
            continue
    return answer

print(solution(name))