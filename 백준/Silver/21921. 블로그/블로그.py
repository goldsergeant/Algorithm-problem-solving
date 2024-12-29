import sys

N,X=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
if max(arr)==0:
    print('SAD')
    exit()

right=0
total=0
answer=(0,0)
for left in range(len(arr)-X+1):
    while right<len(arr) and left+X>right:
        total+=arr[right]
        right+=1

    if total>answer[0]:
        answer=(total,1)
    elif total==answer[0]:
        answer=(total,answer[1]+1)

    total-=arr[left]

print(*answer, sep='\n')