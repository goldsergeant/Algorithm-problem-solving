def solution(triangle):
    answer = 0
    dp=[[-1 for _ in range(len(triangle))] for _ in range(len(triangle))]
    
    def dfs(r,c):
        if r==len(triangle)-1:
            return triangle[r][c]
        if dp[r][c]!=-1:
            return dp[r][c]
        
        dp[r][c]=max(dfs(r+1,c),dfs(r+1,c+1))+triangle[r][c]
    
        return dp[r][c]

    return dfs(0,0)