import sys

N=int(sys.stdin.readline())
numbers=[*map(int,sys.stdin.readline().split())]
answer=0
while len(numbers)>1:
    target=max(numbers)
    idx=numbers.index(target)

    l_diff,r_diff=sys.maxsize,sys.maxsize
    if idx>0:
        l_diff=target-numbers[idx-1]
    if idx<len(numbers)-1:
        r_diff=target-numbers[idx+1]

    if l_diff<r_diff:
        answer+=l_diff
    else:
        answer+=r_diff
    numbers.pop(idx)

print(answer)