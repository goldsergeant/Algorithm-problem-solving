

def solution(n, computers):
    visited = [False for _ in range(n)]
    def dfs(com):
        visited[com]=True
        for connect in range(n):
            if connect!=com and computers[com][connect]==1:
                if visited[connect]==False:
                    dfs(connect)
    answer=0
    for com in range(n):
        if visited[com]==False:
            dfs(com)
            answer+=1
    return answer
