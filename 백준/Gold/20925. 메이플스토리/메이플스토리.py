import sys

N,T=map(int,sys.stdin.readline().split())
exp_infos=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
move_time=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[[0 for _ in range(N)] for _ in range(T+1)] # 시간,노드

# for i in range(N):
#     if exp_infos[i][0]==0:
#         dp[0][i]=exp_infos[i][1]

for t in range(1,T+1):
    for i in range(N):
        # dp[t][i]=dp[t-1][i]+exp_infos[i][1]
        for j in range(N):
            if i==j:
                if dp[t-1][i]>=exp_infos[i][0]:
                    dp[t][i]=max(dp[t][i],dp[t-1][i]+exp_infos[i][1])
            else:
                prev_time=t-move_time[i][j]
                if prev_time>=0 and dp[prev_time][j]-exp_infos[j][1]>=exp_infos[i][0]:
                    dp[t][i]=max(dp[t][i],dp[prev_time][j]+exp_infos[i][1]-exp_infos[j][1])

# for arr in dp:
#     print(arr)
print(max(dp[T]))