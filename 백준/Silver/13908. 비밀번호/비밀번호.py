import itertools
import sys

N,M=map(int,sys.stdin.readline().split())
numbers=set(list(map(int,sys.stdin.readline().split())))
answer=0
visited=[0 for _ in range(9+1)]
def dfs(depth):
    global answer
    if depth==N:
        possible=True
        for n in numbers:
            if visited[n]==0:
                possible=False
                break
        if possible:
            answer+=1
        return

    for i in range(9+1):
        if visited[i]<N:
            visited[i]+=1
            dfs(depth+1)
            visited[i]-=1

dfs(0)
print(answer)