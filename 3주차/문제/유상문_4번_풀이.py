from collections import deque

people = [70, 80, 50, 20, 30]
limit = 100

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) == 1:
            answer += 1
            break
        else:
            if people[0] + people[-1]> limit:
                people.pop()
                answer += 1
            else:
                people.popleft()
                people.pop()
                answer += 1
    return answer

print(solution(people,limit))