import heapq

scoville = [1, 2, 3]
k = 11
# scoville = [1,1,100]
# k = 0
# scoville = [1, 2, 3, 9, 10, 12]
# k=7

def solution(scoville, k) :
    heapq.heapify(scoville)
    result = 0
    while len(scoville)>1:
        heapq.heappush(scoville, heapq.heappop(
            scoville) + heapq.heappop(scoville) * 2)
        result += 1
        if scoville[0] >=k :
            return result
    return -1

print(solution(scoville, k))

# def mix(scobile) :
#     for i in range(len(scobile) - 1) :
#         scobile.sort()
#
#         if k < scobile[0] : return i
#
#         mix_scobile = scobile[0] + scobile[1]*2
#         scobile.remove(scobile[1])
#         scobile.remove(scobile[0])
#         scobile.append(mix_scobile)
#     else :
#         return -1
