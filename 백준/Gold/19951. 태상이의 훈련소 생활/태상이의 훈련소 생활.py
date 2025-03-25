import sys

N,M=map(int,sys.stdin.readline().split())
H=list(map(int,sys.stdin.readline().split()))+[0]
t_sum=[0 for _ in range(N+1)]
for _ in range(M):
    a,b,k=map(int,sys.stdin.readline().split())
    t_sum[a-1]+=k
    t_sum[b]-=k

for i in range(1,len(H)):
    t_sum[i]+=t_sum[i-1]

print(*[H[i]+t_sum[i] for i in range(N)])