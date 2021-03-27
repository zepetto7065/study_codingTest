# 버블정렬
# 시간복잡도: n * n
def bubble_sort(numbers):
    size = len(numbers)

    for i in range(size - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# 선택정렬
# 시간복잡도: n * n
def selection_sort(numbers):
    size = len(numbers)

    for i in range(size - 1):
        min_index = i

        for j in range(i + 1, size):
            if numbers[min_index] > numbers[j]:
                min_index = j

        numbers[min_index], numbers[i] = numbers[i], numbers[min_index]

    return numbers


# 삽입정렬
# 시간복잡도: n * n
def insertion_sort(numbers):
    size = len(numbers)

    for i in range(1, size):
        location = i

        for j in range(i - 1, -1, -1):
            if numbers[j] > numbers[i]:
                location = j
            else:
                break

        tmp = numbers[i]

        for j in range(i, location, -1):
            numbers[j] = numbers[j - 1]

        numbers[location] = tmp

    return numbers


# 퀵정렬
# 시간복잡도
# 평균: n log n
# 최악: n * n

# def quick_sort(numbers):
#     size = len(numbers)
#
#     if size <= 1:
#         return numbers
#
#     pivot = numbers[size // 2]
#     lesser_numbers, equal_numbers, greater_numbers = [], [], []
#
#     for number in numbers:
#         if number < pivot:
#             lesser_numbers.append(number)
#         elif number > pivot:
#             greater_numbers.append(number)
#         else:
#             equal_numbers.append(number)
#
#     return quick_sort(lesser_numbers) + equal_numbers + quick_sort(greater_numbers)

def quick_sort(numbers):
    def sort(low, high):
        if low >= high:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = numbers[(low + high) // 2]

        while low <= high:
            while numbers[low] < pivot:
                low += 1
            while numbers[high] > pivot:
                high -= 1
            if low <= high:
                numbers[low], numbers[high] = numbers[high], numbers[low]
                low, high = low + 1, high - 1

        return low

    sort(0, len(numbers) - 1)

    return numbers


# 합병정렬
# 시간복잡도: n log n

# def merge_sort(numbers):
#     size = len(numbers)
#
#     if size < 2:
#         return numbers
#
#     mid = size // 2
#     front_numbers = merge_sort(numbers[:mid])
#     back_numbers = merge_sort(numbers[mid:])
#
#     merged_numbers = []
#     f = b = 0
#
#     while f < len(front_numbers) and b < len(back_numbers):
#         if front_numbers[f] < back_numbers[b]:
#             merged_numbers.append(front_numbers[f])
#             f += 1
#         else:
#             merged_numbers.append(back_numbers[b])
#             b += 1
#     merged_numbers += front_numbers[f:]
#     merged_numbers += back_numbers[b:]
#
#     return merged_numbers

def merge_sort(numbers):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if numbers[l] < numbers[h]:
                temp.append(numbers[l])
                l += 1
            else:
                temp.append(numbers[h])
                h += 1

        while l < mid:
            temp.append(numbers[l])
            l += 1
        while h < high:
            temp.append(numbers[h])
            h += 1

        for i in range(low, high):
            numbers[i] = temp[i - low]

    sort(0, len(numbers))
    return numbers


print(bubble_sort([5, 4, 3, 2, 1]))

print(selection_sort([5, 4, 3, 2, 1]))

print(insertion_sort([5, 4, 3, 2, 1]))

print(quick_sort([1, 2, 3, 4, 5]))
print(quick_sort([5, 4, 3, 2, 1]))
print(quick_sort([2, 4, 3, 5, 1]))
print(quick_sort([6, 5, 4, 3, 2, 1]))
print(quick_sort([5, 4, 3, 6, 2, 1]))

print(merge_sort([4, 3, 2, 1]))
print(merge_sort([5, 4, 3, 2, 1]))
print(merge_sort([5, 4, 3, 6, 2, 1]))
