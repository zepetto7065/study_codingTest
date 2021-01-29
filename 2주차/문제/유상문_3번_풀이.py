
clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
#clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

def solution(clothes):
    clothedict = {}
    result = 1
    for clothe in clothes:
        key = clothe[1]

        if key in clothedict.keys():
            clothedict[key]=clothedict[key]+1
        else:
            clothedict[key]=1



    for item in clothedict:
        result *= clothedict[item]+1

    return result-1

print(solution(clothes))