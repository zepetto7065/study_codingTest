
n =7
tuple = [(4,60),(4,40),(1,20),(2,50),(3,30),(4,10),(6,5)]
result = []
for i in range(n-1, 0):
    if tuple[0] <= i:
        result.append(tuple[1])


