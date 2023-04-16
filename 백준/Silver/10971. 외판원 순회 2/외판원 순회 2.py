import heapq
import sys

n=int(input())
w=[]
answer=[]
visited=[False for _ in range(n)]
for _ in range(n):
    w.append(list(map(int,sys.stdin.readline().split())))

def dfs(depth,node,cost,start):
    if depth==n:
        if w[node][start]!=0:
            answer.append(cost+w[node][start])
        return

    for next_node in range(n):
        if not visited[next_node] and w[node][next_node]!=0:
            visited[next_node]=True
            dfs(depth+1,next_node,cost+w[node][next_node],start)
            visited[next_node]=False


for i in range(n):
    visited[i]=True
    dfs(1,i,0,i)
    visited[i]=False

print(min(answer))