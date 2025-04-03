import sys
from bisect import bisect_left

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

arr=[A[0]]
for num in A[1:]:
    if num>arr[-1]:
        arr.append(num)
        continue

    idx=bisect_left(arr,num)
    arr[idx]=num

print(len(arr))