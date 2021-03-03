all_value = input().split('-')
all_list = []
for i in all_value:
    num = 0
    value = i.split('+')
    for j in value:
        num += int(j)
    all_list.append(num)
final_value = all_list[0]
for i in range(1, len(all_list)):
    final_value -= all_list[i]
print(final_value)
