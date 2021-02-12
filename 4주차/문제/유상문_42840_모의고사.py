answers = [1, 2, 3, 4, 5]


def makePatten(length, sample) :
    sample = sample * int(length / len(sample) + 1)
    return sample[0 :length]

def checkAnswer(answers, supo):
    result = 0

    for i in range(len(answers)) :
        if answers[i] == supo[i]:
            result += 1

    return result





def solution(answers) :
    answer = []
    length = len(answers)
    # 답안지 만들기
    supo1 = makePatten(length, list(range(1, 6)))
    supo2 = makePatten(length, [2, 1, 2, 3, 2, 4, 2, 5])
    supo3 = makePatten(length, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    #채점하기
    result1 = checkAnswer(answers, supo1)
    result2 = checkAnswer(answers, supo2)
    result3 = checkAnswer(answers, supo3)

    results = [result1, result2, result3]

    for i , n in enumerate(results):
        if n == max(results):
            answer.append(i+1)


    return answer


print(solution(answers))
