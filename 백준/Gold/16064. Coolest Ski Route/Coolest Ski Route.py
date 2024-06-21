import collections
import sys

def dfs(node):
    if income[node]==0:
        return 0
    if dp[node]!=-1:
        return dp[node]

    dp[node]=0
    for next_node,next_cost in reverse_graph[node]:
        dp[node]=max(dp[node],dfs(next_node)+next_cost)

    return dp[node]

N,M=map(int,sys.stdin.readline().split())
income=[0 for _ in range(N+1)]
outcome=[0 for _ in range(N+1)]
reverse_graph=collections.defaultdict(list)
dp=[-1 for _ in range(N+1)]
answer=0
for _ in range(M):
    s,t,c=map(int,sys.stdin.readline().split())
    outcome[s]+=1
    income[t]+=1
    reverse_graph[t].append((s,c))

for i in range(1,N+1):
    if outcome[i]==0:
        answer=max(answer,dfs(i))

print(answer)