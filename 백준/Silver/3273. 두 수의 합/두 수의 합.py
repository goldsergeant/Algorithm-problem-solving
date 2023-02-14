import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())
arr.sort()
answer = 0
left=0
right=len(arr)-1
while left<right:
    if arr[left]+arr[right]>x:
        right-=1
    elif arr[left]+arr[right]<x:
        left+=1
    else:
        answer+=1
        left+=1
print(answer)
