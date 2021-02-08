
n = int(input())
pi = list(map(int,input().split()))


list = []
pi.sort()

for i in range(n) :
    if i == 0 :
        list.append(pi[i])
    else:
        sum = pi[i] + list[i-1]
        list.append(sum)

result = 0
for num in list:
    result += num

print(result)