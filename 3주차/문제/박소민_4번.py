from collections import deque
# 효율성1번 시간초과때문에 deque사용


def solution(people, limit):
    people.sort()
    people = deque(people)
    cnt = 0

    while people:
        if len(people) == 1:
            cnt += 1
            break
        else:
            if people[0]+people[-1] > limit:
                people.pop()
                cnt += 1
            else:
                people.pop()
                people.popleft()
                cnt += 1
    return cnt
