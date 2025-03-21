import sys

N, T = map(int, sys.stdin.readline().split())
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move_times = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
dp = [[0 for _ in range(T + 1)] for _ in range(N)] # 사냥터, 시간
for time in range(1,T+1):
    for i in range(N):
        if dp[i][time-1]>=fields[i][0]:
            dp[i][time]=dp[i][time-1]+fields[i][1]
        for j in range(N):
            if i==j:
                continue
            move_time=move_times[i][j]
            if time-move_time>=0 and dp[j][time-move_time]-fields[j][1]>=fields[i][0]:
                dp[i][time]=max(dp[i][time],dp[j][time-move_time]-fields[j][1]+fields[i][1])


answer=0
for i in range(N):
    answer=max(answer,dp[i][T])
print(answer)


