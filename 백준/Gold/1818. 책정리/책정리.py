import sys
from bisect import bisect_left
N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
arr=[numbers[0]]
for i in range(1,len(numbers)):
    if numbers[i]>arr[-1]:
        arr.append(numbers[i])
    else:
        idx=bisect_left(arr,numbers[i])
        arr[idx]=numbers[i]

print(N-len(arr))