import sys

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

def get_mixed_value(tup:tuple):
    return abs(sum(tup))

left=0
right=N-1
answer=(sys.maxsize,sys.maxsize)

while left<right:
    if get_mixed_value((arr[left],arr[right]))<=get_mixed_value(answer):
        answer=(arr[left],arr[right])

    mid=arr[left]+arr[right]
    if mid<0:
        left+=1
    else:
        right-=1


print(*answer)