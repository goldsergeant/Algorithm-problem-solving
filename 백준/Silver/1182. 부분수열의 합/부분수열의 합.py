import sys

n,s=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
answer=0
visited=[False for _ in range(n)]
def dfs(total,index):
    global answer
    if total==s:
        answer+=1

    for i in range(index+1,n):
        if not visited[i]:
            visited[i]=True
            dfs(total+arr[i],i)
            visited[i]=False

for i in range(n):
    visited[i]=True
    dfs(arr[i],i)
    visited[i]=False

print(answer)