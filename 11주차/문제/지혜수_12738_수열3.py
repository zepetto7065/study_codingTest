# bisect.bisect_left(a, x, lo=0, hi=len(a))
# 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다. 
# 매개 변수 lo 와 hi는 고려해야 할 리스트의 부분집합을 지정하는 데 사용될 수 있습니다
# 기본적으로 전체 리스트가 사용됩니다. x가 a에 이미 있으면, 삽입 위치는 기존 항목 앞(왼쪽)이 됩니다. 
# 반환 값은 a가 이미 정렬되었다고 가정할 때 list.insert()의 첫 번째 매개 변수로 사용하기에 적합합니다.

# 반환된 삽입 위치 i는 배열 a를 이분하여, 왼쪽은 all(val < x for val in a[lo:i]), 
# 오른쪽은 all(val >= x for val in a[i:hi])이 되도록 만듭니다.

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))

# A: [10, 20, 15, 30, 20, 50] -> dp: [10, 15, 20, 50]