import sys

N, C = map(int , sys.stdin.readline().split())
home = [int(sys.stdin.readline()) for _ in range(N)]

#해당 거리를 유지하며 공유기가 몇개 설치?
def router_counter(distance):
    count = 1
    cur_house = home[0]
    for i in range(1, N):
        if cur_house + distance <= home[i]:
            count += 1
            cur_house = home[i]
    return count

home = sorted(home)
start, end = 1, home[-1] - home[0]

while start <= end:
    mid = (start+end)//2

    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else :
        end = mid - 1

print(answer)