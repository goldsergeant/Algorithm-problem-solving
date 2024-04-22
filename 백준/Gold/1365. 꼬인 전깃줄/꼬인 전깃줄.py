import sys
from bisect import bisect_left

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
arr=[numbers[0]]
answer=1
for num in numbers[1:]:
    if num>arr[-1]:
        arr.append(num)
    else:
        idx=bisect_left(arr,num)
        arr[idx]=num
    answer=max(answer,len(arr))

print(N-answer)