K = int(input())
a = []
for _ in range(K):
    n = int(input())
    if a and n == 0:
        a.pop()
    else:
        a.append(n)

print(sum(a))  # 리스트 a에 있는 원소를 모두 더해서 print
