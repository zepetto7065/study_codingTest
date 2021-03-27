word = input()

length = len(word)
words = []

for i in range(length):
    words.append(word[i:])

words.sort()

for i in range(length):
    print(words[i])
