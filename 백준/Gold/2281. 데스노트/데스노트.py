import sys

N, M = map(int, sys.stdin.readline().split())
name_lengths =[int(sys.stdin.readline()) for _ in range(N)]
dp=[sys.maxsize for _ in range(N)]
dp[N-1]=0
for i in range(N-2,-1,-1):
    t_sum = -1
    for j in range(i,N):
        t_sum+=1 + name_lengths[j]
        if t_sum>M:
            break
        if j==N-1:
            dp[i]=0
        else:
            dp[i]=min(dp[i],dp[j+1]+(M-t_sum)**2)

print(dp[0])
