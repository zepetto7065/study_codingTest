def solution(phone_book):
    phone_book.sort()
    for x, y in zip(phone_book, phone_book[1:]):
        if x == y[:len(x)]:
            return False
    return True