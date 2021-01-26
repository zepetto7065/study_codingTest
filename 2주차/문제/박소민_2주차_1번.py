
def solution(participant, completion):
    participant.sort()
    completion.sort()
    a = len(completion)

    for i in range(a):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
