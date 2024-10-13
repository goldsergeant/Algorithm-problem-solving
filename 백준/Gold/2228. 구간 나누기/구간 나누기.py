# import sys
#
# N,M=map(int,sys.stdin.readline().split())
# numbers=[0]+[int(sys.stdin.readline()) for _ in range(N)]
# t_sum=[numbers[0]]
# dp=[[-sys.maxsize for _ in range(M+1)] for _ in range(N+1)]
# for num in numbers[1:]:
#     t_sum.append(t_sum[-1]+num)
#
# dp[1][1]=numbers[1]
#
# for i in range(2,N+1):
#     for j in range(1,M+1):
#         dp[i][j]=dp[i-1][j]
#         if j == 1:
#             dp[i][j] = max(dp[i][j], t_sum[i])
#
#         for m in range(1,i-1):
#             dp[i][j]=max(dp[i][j],dp[m][j-1]+t_sum[i]-t_sum[m+1])
# print(dp[N][M])

import sys

N,M=map(int,sys.stdin.readline().split())
numbers=[0]+[int(sys.stdin.readline()) for _ in range(N)]
con=[[-sys.maxsize for _ in range(M+1)] for _ in range(N+1)]
not_con=[[-sys.maxsize for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    con[i][0]=0
    not_con[i][0]=0
for i in range(1,N+1):
    for j in range(1,min(M, (i+1)//2)+1):
        not_con[i][j]=max(not_con[i-1][j],con[i-1][j])
        con[i][j]=max(con[i-1][j],not_con[i-1][j-1])+numbers[i]

print(max(not_con[N][M],con[N][M]))