import collections
import sys

N,M,K=map(int,sys.stdin.readline().split())
candies=[0]+list(map(int,sys.stdin.readline().split()))
graph=collections.defaultdict(list)
visited=[False]*(N+1)
answer=0
union_candies=[]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start,total,nodes_cnt):
    q=collections.deque([start])
    visited[start]=True
    while q:
        node=q.popleft()
        total+=candies[node]
        nodes_cnt+=1

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append(next_node)

    return total,nodes_cnt


for i in range(1,N+1):
    if not visited[i]:
        union_candies.append(bfs(i,0,0))

dp=[[0 for _ in range(K)] for _ in range(len(union_candies)+1)]

min_len=0
for i in range(1,len(union_candies)+1):
    candies,nodes_cnt=union_candies[i-1]
    min_len+=nodes_cnt
    for j in range(1,min(K,min_len+1)):
        if j-nodes_cnt<0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-nodes_cnt]+candies)

print(dp[-1][K-1])