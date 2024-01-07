import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
left=0
right=N-1
answer=sys.maxsize
while left<right:
    mid=numbers[left]+numbers[right]
    if abs(mid)<abs(answer):
        answer=mid
    if mid>0:
        right-=1
    elif mid<0:
        left+=1
    else:
        break

print(answer)