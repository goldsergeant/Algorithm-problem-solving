import collections
import sys

N,D,K,C=map(int,sys.stdin.readline().split())
numbers=[int(sys.stdin.readline()) for _ in range(N)]
numbers+=numbers
left=0
right=-1
counter=[0 for _ in range(D+1)]
counter[C]=1
cnt=1
answer=0
for _ in range(K):
    right+=1
    if counter[numbers[right]]==0:
        cnt+=1

    counter[numbers[right]]+=1
    answer = max(answer, cnt)

while right<len(numbers)-1:
    counter[numbers[left]]-=1
    if counter[numbers[left]]==0:
        cnt-=1
    left+=1

    right+=1
    if counter[numbers[right]]==0:
        cnt+=1
    counter[numbers[right]]+=1
    answer = max(answer, cnt)

print(answer)