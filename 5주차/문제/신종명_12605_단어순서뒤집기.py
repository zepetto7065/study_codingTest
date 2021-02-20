count = int(input())

for i in range(count):
    words = input().split()
    print("Case #%d: %s" % (i + 1, ' '.join(words[::-1])))
