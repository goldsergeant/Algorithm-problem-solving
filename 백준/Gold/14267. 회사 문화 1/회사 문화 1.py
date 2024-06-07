import collections
import sys
sys.setrecursionlimit(100000+1)

def get_score(node):
    if node==parent[node]:
        return 0
    if dp[node]!=-1:
        return dp[node]

    dp[node]=score[node]+get_score(parent[node])
    return dp[node]

N,M=map(int,sys.stdin.readline().split())
parent=[0]+list(map(int,sys.stdin.readline().split()))
parent[1]=1
score=[0 for _ in range(N+1)]
dp=[-1 for _ in range(N+1)]

for _ in range(M):
    node,how_many=map(int,sys.stdin.readline().split())
    score[node]+=how_many

for i in range(1,N+1):
    print(get_score(i),end=' ')