import sys


def dfs(idx):
    global answer
    if idx == 2*N:
        answer += 1
        return

    if nums[idx]!=0:
        dfs(idx+1)
        return

    for i in range(1,N+1):
        if not visited[i] and idx+i+1<2*N and nums[idx+i+1]==0:
            nums[idx+i+1]=nums[idx]=i
            visited[i]=True
            dfs(idx+1)
            nums[idx+i+1]=nums[idx]=0
            visited[i]=False



N, X, Y = map(int, sys.stdin.readline().split())
tmp = Y - X - 1
nums = [0 for _ in range(2 * N)]
nums[Y-1]=nums[X-1]=tmp
visited = [False for _ in range(N + 1)]
visited[tmp]=True
answer = 0
dfs(0)
print(answer)
