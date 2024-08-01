from heapq import heappush, heappop
import sys


def solution(alp, cop, problems):
    problems.append([0, 0, 0, 1, 1])
    problems.append([0, 0, 1, 0, 1])
    goal_alp=0
    goal_cop=0
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        goal_alp=max(goal_alp,alp_req)
        goal_cop=max(goal_cop,cop_req)
    
    alp=min(goal_alp,alp)
    cop=min(goal_cop,cop)
    dp=[[sys.maxsize for _ in range(goal_cop+1)] for _ in range(goal_alp+1)]
    dp[alp][cop]=0
    
    for i in range(alp,goal_alp+1):
        for j in range(cop,goal_cop+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>=alp_req and j>=cop_req:
                    next_alp,next_cop=min(i+alp_rwd,goal_alp),min(j+cop_rwd,goal_cop)
                    dp[next_alp][next_cop]=min(dp[next_alp][next_cop],dp[i][j]+cost)
                
    return dp[-1][-1]

print(solution(10, 10, []))
print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))
