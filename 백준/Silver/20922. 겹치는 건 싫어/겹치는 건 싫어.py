import sys

N,K=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
counter=[0 for _ in range(100000+1)]
answer=1

right=0
for left in range(N):
    while right<N:
        if counter[arr[right]]>=K:
            counter[arr[left]]-=1
            left+=1
            break
        answer = max(answer, right - left + 1)
        counter[arr[right]]+=1
        right+=1


print(answer)