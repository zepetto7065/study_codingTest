
a = int(input())

alist = list(map(int, input().split(' ')))
blist = []
blist.append(alist[0])
for i in alist:
    if blist[-1] < i:
        blist.append(i)
    else:
        left = 0
        right = len(blist)-1
        while left < right:
            mid = (left+right)//2
            if blist[mid] < i:
                left = mid+1
            else:
                right = mid
        blist[right] = i
print(len(blist))

# for i in alist:
#     if i in blist:
#         continue
#     else:
#         blist.append(i)
# print(len(blist))
