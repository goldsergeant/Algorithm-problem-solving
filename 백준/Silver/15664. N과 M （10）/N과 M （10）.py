import sys

N,M=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
visited=[False for _ in range(N)]
answer=set()

def dfs(nums,depth):
    if depth>=M:
        answer.add(tuple(nums))
        return

    for i in range(N):
        if not nums or (not visited[i] and numbers[i]>=nums[-1]):
            visited[i]=True
            dfs(nums+[numbers[i]],depth+1)
            visited[i]=False

for i in range(N):
    visited[i]=True
    dfs([numbers[i]],1)
    visited[i]=False

for arr in sorted(answer):
    print(*arr)