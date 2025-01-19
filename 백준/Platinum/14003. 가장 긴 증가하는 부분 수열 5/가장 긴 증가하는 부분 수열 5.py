import sys
from bisect import bisect_left

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
max_nums=[numbers[0]]
trace=[0 for _ in range(N)]

for i in range(1,len(numbers)):
    if numbers[i]>max_nums[-1]:
        max_nums.append(numbers[i])
        trace[i]=len(max_nums)-1
    else:
        idx=bisect_left(max_nums,numbers[i])
        max_nums[idx]=numbers[i]
        trace[i]=idx

print(len(max_nums))
last_idx=len(max_nums)-1
answer=[]
for i in range(len(trace)-1,-1,-1):
    if trace[i]==last_idx:
        answer.append(numbers[i])
        last_idx-=1

print(*answer[::-1])