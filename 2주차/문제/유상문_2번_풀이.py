phone_book = list(map(str, input().split()))

def solution(phone_book):
    phone_book.sort()
    result =  True
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1] :
            result = False

    return result

print(solution(phone_book))