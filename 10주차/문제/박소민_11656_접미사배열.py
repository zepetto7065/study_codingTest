
s = list(input())

sort_list = []

while s:

    sort_list.append("".join(s))
    s.pop(0)

sort_list.sort()
for i in sort_list:
    print(i)
