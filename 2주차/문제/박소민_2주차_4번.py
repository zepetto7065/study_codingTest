import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # for num in scoville:
    #     heapq.heappush(hea,num)
    while scoville[0] < K and len(scoville) >= 2:
        heapq.heappush(scoville, heapq.heappop(
            scoville)+heapq.heappop(scoville)*2)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1
