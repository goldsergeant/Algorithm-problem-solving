import sys

T=int(sys.stdin.readline())
for _ in range(T):
    args=[*map(int,sys.stdin.readline().split())]
    N=args[0]
    numbers=sorted(args[1:])

    max_num_dp=[[0 for _ in range(N)] for _ in range(N)]
    t_sum=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(i,N):
            if i==j:
                max_num_dp[i][j]=numbers[i]
                t_sum[i][j]=numbers[i]
            else:
                max_num_dp[i][j]=max(max_num_dp[i][j-1],numbers[j])
                t_sum[i][j]=t_sum[i][j-1]+numbers[j]

    answer=0
    for space in range(2,N+1):
        tmp=sys.maxsize
        for i in range(N-space+1):
            j=i+space-1
            tmp=min(tmp,max_num_dp[i][j]*space-t_sum[i][j])
        answer+=tmp

    print(answer)