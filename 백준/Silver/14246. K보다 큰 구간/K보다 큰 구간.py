import sys

n=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())
answer=0
left=0
right=0
total=0
while right<=n:
    if total>k:
        answer+=n-right+1
        total-=numbers[left]
        left+=1
    elif right>=n:
        break
    elif total<=k:
        total+=numbers[right]
        right+=1


print(answer)