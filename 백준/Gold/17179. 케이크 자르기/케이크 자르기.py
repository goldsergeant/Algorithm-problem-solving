import sys


def check(cnt, mid):
    prev = 0
    for i in range(len(numbers)):
        if numbers[i] - prev >= mid:
            cnt -= 1
            prev = numbers[i]
    return True if cnt < 0 else False


N, M, L = map(int, sys.stdin.readline().split())
numbers = list(int(sys.stdin.readline()) for _ in range(M)) + [L]
for _ in range(N):
    cnt = int(sys.stdin.readline())
    left,right=0,L
    while left+1<right:
        mid=(left+right)//2
        if check(cnt, mid):
            left=mid
        else:
            right=mid

    print(left)