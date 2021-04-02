def binary_search(list, target, left, right):
    middle_index = (left + right) // 2
    middle_value = list[middle_index]

    if target == middle_value:
        print(middle_index + 1)
        return
    elif target < middle_value:
        binary_search(list, target, left, middle_index - 1)
    elif target > middle_value:
        binary_search(list, target, middle_index + 1, right)
    else:
        print('Not Found')


target = 5
list = [1, 2, 3, 4, 5]
list.sort()
size = len(list)

binary_search(list, target, 0, size - 1)

left = 0
right = size - 1;
while left <= right:
    mid_index = (left + right) // 2
    if list[mid_index] == target:
        print(mid_index + 1)
        break;
    elif list[mid_index] < target:
        left = mid_index + 1
    else:
        right = mid_index - 1
