# 2
# 3
# hat headgear
# sunglasses eyewear
# turban headgear
# 3
# mask face
# sunglasses face
# makeup face

n = int(input())

clothes = []

for i in range(n) :
    len = int(input())
    one_clothe = []
    for j in range(len) :
        one_clothe.append(input().split())
    clothes.append(one_clothe)

result_list = []


def solution(clothes) :
    for i in range(n) :
        result = 1
        clothedict = {}
        temp_clothes = clothes[i]
        for clothe in temp_clothes :
            key = clothe[1]

            if key in clothedict.keys() :
                clothedict[key] = clothedict[key] + 1
            else :
                clothedict[key] = 1

        for item in clothedict :
            result *= clothedict[item] + 1

        result_list.append(result - 1)
        clothedict.clear()

    for _ in result_list:
        print(_)


solution(clothes)
