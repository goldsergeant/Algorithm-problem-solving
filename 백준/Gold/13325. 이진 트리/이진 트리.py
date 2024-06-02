import sys

def dfs(idx,height):
    global answer
    if height==tree_height:
        answer+=edges[idx]
        return edges[idx]
    left=dfs(idx*2,height+1)
    right=dfs(idx*2+1,height+1)

    answer+=edges[idx]+abs(left-right)
    dp[idx]=edges[idx]+max(left,right)
    return dp[idx]


tree_height=int(sys.stdin.readline())
edges=[0,0]+list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(len(edges))]
answer=0
dfs(1,0)
print(answer)