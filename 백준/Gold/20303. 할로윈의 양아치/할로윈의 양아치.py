import collections
import sys

N,M,K=map(int,sys.stdin.readline().split())
candies=[0]+list(map(int,sys.stdin.readline().split()))
union_candies=[[0,0] for _ in range(N+1)]
parent=[i for i in range(N+1)]
dp=[0 for _ in range(K)]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    union(a,b)

for i in range(1,N+1):
    root=find(i)
    union_candies[root][0]+=1
    union_candies[root][1]+=candies[i]

for i in range(1,N+1):
    if parent[i]!=i:
        continue
    for j in range(K-1,union_candies[i][0]-1,-1):
        dp[j]=max(dp[j],dp[j-union_candies[i][0]]+union_candies[i][1])

print(max(dp))