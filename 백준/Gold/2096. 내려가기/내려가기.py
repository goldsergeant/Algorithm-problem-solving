import sys

N=int(sys.stdin.readline())
scores=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
max_dp=[[0]*3 for _ in range(2)]
min_dp=[[0]*3 for _ in range(2)]
max_dp[0]= scores[0].copy()
min_dp[0]= scores[0].copy()

for i in range(1,N ):
    idx=i%2
    for x in range(3):
        max_tmp=0
        min_tmp=sys.maxsize
        for dx in (-1,0,1):
            nx=x+dx
            if 0<=nx<3:
                max_tmp=max(max_tmp,max_dp[idx-1][nx])
                min_tmp=min(min_tmp,min_dp[idx-1][nx])

        max_dp[idx][x]=max_tmp+scores[i][x]
        min_dp[idx][x]=min_tmp+scores[i][x]

print(max(max_dp[N%2-1]),min(min_dp[N%2-1]))
