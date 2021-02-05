from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while (people):
        answer += 1
        tmp = limit - people.pop()
        if len(people)!=0 and people[0] <= tmp:
            people.popleft()
    return answer