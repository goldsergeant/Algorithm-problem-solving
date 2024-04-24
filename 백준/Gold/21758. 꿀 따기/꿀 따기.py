import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
t_sum=[0 for _ in range(N)]
t_sum[0]=numbers[0]
answer=0
for i in range(1,N):
    t_sum[i]=t_sum[i-1]+numbers[i]

for i in range(1,N-1): # 벌 벌 꿀통
    bee1=t_sum[-1]-numbers[0]-numbers[i]
    bee2=t_sum[-1]-t_sum[i]
    answer=max(answer,bee1+bee2)
for i in range(1,N-1): # 벌 꿀통 벌
    bee1=t_sum[i]-numbers[0]
    bee2=t_sum[-1]-t_sum[i-1]-numbers[-1]
    answer=max(answer,bee1+bee2)
for i in range(1,N-1): # 꿀통 벌 벌
    bee1=t_sum[i]-numbers[i]
    bee2=t_sum[-1]-numbers[-1]-numbers[i]
    answer=max(answer,bee1+bee2)

print(answer)