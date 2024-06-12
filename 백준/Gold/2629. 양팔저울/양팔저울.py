import sys

weight_cnt=int(sys.stdin.readline())
weights=[0]+[*map(int,sys.stdin.readline().split())]
total_weight=sum(weights)
check_cnt=int(sys.stdin.readline())
marbles=[0]+[*map(int,sys.stdin.readline().split())]
dp=[[False for _ in range(total_weight+1)] for _ in range(len(weights))]

dp[0][0]=True
for i in range(1,len(weights)):
    dp[i][0]=True
    for j in range(total_weight,-1,-1):
        if not dp[i-1][j]:
            continue
        dp[i][j]=True
        for d_weight in (-j,j):
            n_weight=abs(weights[i]+d_weight)
            if n_weight<=total_weight:
                dp[i][n_weight]=True

print(*map(lambda x:'Y' if x<=total_weight and dp[-1][x] else 'N',marbles[1:]))