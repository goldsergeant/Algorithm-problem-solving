import sys

n=int(input())
arr=[]
answer=sys.maxsize
visited=[False for _ in range(n)]

def dfs(depth):
    global answer
    start=0
    link=0
    if depth==n:
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start+=arr[i][j]
                elif not visited[i] and not visited[j]:
                    link+=arr[i][j]
        diff=abs(start-link)
        if diff<answer:
            answer=diff
        return

    visited[depth]=True
    dfs(depth+1)
    visited[depth]=False
    dfs(depth+1)


for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dfs(0)

print(answer)