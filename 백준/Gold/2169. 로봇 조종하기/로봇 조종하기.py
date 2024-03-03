import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-sys.maxsize for _ in range(M)] for _ in range(N)]

dp[0][0]=board[0][0]
for j in range(1,M):
    dp[0][j]=dp[0][j-1]+board[0][j]

for i in range(1,N):
    left_to_right=dp[i][:]
    right_to_left=dp[i][:]

    left_to_right[0]=dp[i-1][0]+board[i][0]
    for j in range(1,M):
        left_to_right[j]=max(dp[i-1][j],left_to_right[j-1])+board[i][j]

    right_to_left[M-1]=dp[i-1][M-1]+board[i][M-1]
    for j in range(M-2,-1,-1):
        right_to_left[j]=max(dp[i-1][j],right_to_left[j+1])+board[i][j]

    for j in range(M):
        dp[i][j]=max(left_to_right[j],right_to_left[j])


print(dp[N-1][M-1])