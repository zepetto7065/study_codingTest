def solution(phone_book):
    phone_book.sort()
    a = len(phone_book)
    for i in range(0, a):
        for j in range(i+1, a):
            if phone_book[i] in phone_book[j]:
                return False
    return True
