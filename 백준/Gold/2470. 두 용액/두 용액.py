import sys

mini=(1000000000,1000000000)
n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
left=0
right=len(arr)-1
while left<right:
    mini = (arr[left], arr[right]) if abs(arr[left] + arr[right]) < abs(mini[0] + mini[1]) else mini

    if arr[left]+arr[right]<0:
        left+=1
    elif arr[left]+arr[right]>0:
        right-=1

    else:
        print(arr[left],arr[right])
        exit()
print(*mini)