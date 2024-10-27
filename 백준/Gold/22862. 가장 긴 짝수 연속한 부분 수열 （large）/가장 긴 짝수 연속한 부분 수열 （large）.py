import sys

N,K=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))

left=0
right=0
answer=0

tmp=0
while right<len(numbers):
    if numbers[right]%2==0:
        right+=1
        tmp+=1
    else:
        if K==0:
            if numbers[left]%2==1:
                K+=1
            else:
                tmp-=1
            left+=1
        else:
            K-=1
            right+=1

    answer=max(answer,tmp)

print(answer)