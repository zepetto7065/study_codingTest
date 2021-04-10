import sys
sys.stdin = open("input.txt", "r")
n = int(input())
t_list = []
for _ in range(n):
    t_list.append(list(map(int, input().split(' '))))

for i in range(1, n):
    for j in range(len(t_list[i])):
        if j == 0:
            t_list[i][j] = t_list[i][j]+t_list[i-1][j]
        elif j == len(t_list[i])-1:
            t_list[i][j] = t_list[i][j]+t_list[i-1][j-1]
        else:
            t_list[i][j] = max(t_list[i-1][j-1], t_list[i-1][j])+t_list[i][j]
print(t_list)
print(max(t_list[n-1]))
