import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))
visited=[False for _ in range(N)]
answer=[]
def get_left(idx):
    for i in range(idx-1,-1,-1):
        if not visited[i]:
            return arr[i]

def get_right(idx):
    for i in range(idx+1,N):
        if not visited[i]:
            return arr[i]

def dfs(depth,energy):
    if depth==N-2:
        answer.append(energy)

    for i in range(1,N-1):
        if not visited[i]:
            visited[i]=True
            dfs(depth+1,energy+get_left(i)*get_right(i))
            visited[i]=False

for i in range(1,N-1):
    visited[i]=True
    dfs(1,arr[i-1]*arr[i+1])
    visited[i]=False

print(max(answer))