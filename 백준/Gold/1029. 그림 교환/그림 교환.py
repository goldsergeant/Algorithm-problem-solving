import sys

def dfs(last_person,last_price,people_bit):
    if dp[last_person][last_price][people_bit]!=-1:
        return dp[last_person][last_price][people_bit]

    dp[last_person][last_price][people_bit]=1

    for i in range(N):
        if (1<<i)&people_bit:
            continue
        if last_price<=prices[last_person][i]:
            n_bit=people_bit|(1<<i)
            dp[last_person][last_price][people_bit]=max(dp[last_person][last_price][people_bit],dfs(i,prices[last_person][i],n_bit)+1)

    return dp[last_person][last_price][people_bit]

N=int(sys.stdin.readline())
prices=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dp=[[[-1 for _ in range(1<<N)] for _ in range(9+1)] for _ in range(N)] # 마지막 구매자,마지막 가격, 현재 산 사람들
print(dfs(0,0,1))
