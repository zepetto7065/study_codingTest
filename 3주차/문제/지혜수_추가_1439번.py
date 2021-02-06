k = input()
idx = 0
cnt = 1
length = len(k)-1

while (idx != length):
    if k[idx] != k[idx+1]:
        cnt += 1
    idx += 1
print(cnt//2)