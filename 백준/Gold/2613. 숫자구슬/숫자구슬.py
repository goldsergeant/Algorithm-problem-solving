import sys

N, M = map(int, sys.stdin.readline().split())
marbles = list(map(int, sys.stdin.readline().split()))


def is_possible(max_total):
    total, group_cnt = 0, 1
    for marble in marbles:
        total += marble
        if total > max_total:
            group_cnt += 1
            total = marble

    return group_cnt <= M


def print_answer(max_total):
    arr=[]
    total = 0
    marble_cnt = 0
    for i in range(len(marbles)):
        total += marbles[i]
        if total > max_total:
            arr.append(marble_cnt)
            total = marbles[i]
            marble_cnt=0
        marble_cnt+=1
        if N-i==M-len(arr):
            break

    while len(arr)<M:
        arr.append(marble_cnt)
        marble_cnt=1

    print(max_total)
    print(*arr)

left = max(marbles)
right = sum(marbles)

while left<=right:
    mid=(left+right)//2

    if is_possible(mid):
        right=mid-1
    else:
        left=mid+1

print_answer(left)