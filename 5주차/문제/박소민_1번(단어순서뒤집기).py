import sys
sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(1, n+1):
    case_value = ''
    case = list(map(str, input().split(' ')))
    case = case[::-1]
    for a in case:
        case_value += a
        case_value += ' '
    print("Case #{i}: {list}".format(i=i, list=case_value))
