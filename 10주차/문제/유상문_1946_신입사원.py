import sys
import heapq

input = sys.stdin.readline
# 테스트 케이스 입력받기
t = int(input())
for i in range(t) :
    # 지원자 수 입력받기
    n = int(input())
    rank = []
    for i in range(n) :
        a, b = map(int, input().split())
        heapq.heappush(rank, (a, b))

    rank.sort()
    # 신입사원 변수
    new = 0
    prev = 9999999
    for k in rank :
        docu, meet = k
        # 서류 점수는 장랼되어 이미 적으니 면접의 순위가 이전 것 보다 면접 순위가 작으면 가능
        if meet < prev :
            new += 1
            prev = meet

    # 신입사원수 출력하기
    print(new)