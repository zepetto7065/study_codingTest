import heapq

def solution(s, k):
    answer = 0
    heapq.heapify(s)
    while s[0] < k:
        heapq.heappush(s, heapq.heappop(s) + (heapq.heappop(s)*2))
        answer += 1
        if len(s) == 1 and s[0] < k:
            return -1
    return answer