import sys

n, c = map(int, input().split())
routers = []
answer = 1
for _ in range(n):
    routers.append(int(sys.stdin.readline().rstrip()))

routers.sort()


def can_install(distance):
    cnt = 1
    prev = routers[0]
    for i in range(1, n):
        if routers[i] - prev >= distance:
            cnt += 1
            prev = routers[i]

    return True if cnt >= c else False

left=1
right=routers[-1]-routers[0]
while left<=right:
    mid=(left+right)//2
    if can_install(mid):
        answer=max(answer,mid)
        left=mid+1
    else:
        right=mid-1

print(answer)