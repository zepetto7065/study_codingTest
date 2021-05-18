import sys
sys.stdin = open("input.txt", "r")
for _ in range(3):
    a = list(map(int, input().split(' ')))
    count_bae = a.count(0)
    count_li = a.count(1)

    if count_bae == 1 and count_li == 3:
        print("A")
    elif count_bae == 2 and count_li == 2:
        print("B")
    elif count_bae == 3 and count_li == 1:
        print("C")
    elif count_bae == 4:
        print("D")
    else:
        print("E")
