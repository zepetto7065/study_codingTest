import collections

participant = list(map(str,input().split()))
completion = list(map(str,input().split()))
temp = []
# 아래 풀이는 시간초과
# def solution(participant, completion) :
#     participant.sort()
#     completion.sort()
#     for i in participant:
#
#     return participant[i]

# 이것도 시간초과
# def solution(participant, completion):
#     for _ in completion:
#         if _ in participant:
#             participant.remove(_)
#     return participant[0]

#collctions의 counter 함수
def solution(participant, completion) :
    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result)[0]

print(solution(participant, completion))
