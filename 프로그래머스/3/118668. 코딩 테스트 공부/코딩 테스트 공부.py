import sys

def solution(alp, cop, problems):
    answer = sys.maxsize
    target_alp=max(problems,key=lambda x:x[0])[0]
    target_cop=max(problems,key=lambda x:x[1])[1]
    dp = [[sys.maxsize for _ in range(target_cop+1)] for _ in range(target_alp+1)]  # alp, cop

    alp=min(alp,target_alp)
    cop=min(cop,target_cop)
    dp[alp][cop]=0

    for a in range(alp,target_alp+1):
        for c in range(cop,target_cop+1):
            if a<target_alp:
                dp[a+1][c]=min(dp[a+1][c],dp[a][c]+1)
            if c<target_cop:
                dp[a][c+1]=min(dp[a][c+1],dp[a][c]+1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a>=alp_req and c>=cop_req:
                    n_alp=min(target_alp,a+alp_rwd)
                    n_cop=min(target_cop,c+cop_rwd)
                    dp[n_alp][n_cop]=min(dp[n_alp][n_cop],dp[a][c]+cost)

    return dp[target_alp][target_cop]