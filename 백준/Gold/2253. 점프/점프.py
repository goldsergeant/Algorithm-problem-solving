import collections
import sys

n, m = map(int, sys.stdin.readline().split())
broken_stones = []
dx=[-1,0,1]
visited=[[] for _ in range(n+1)]
for _ in range(m):
    broken_stones.append(int(sys.stdin.readline()))

dp = [sys.maxsize for _ in range(n + 1)]
for stone in broken_stones:
    dp[stone] = -1

q = collections.deque()
q.appendleft((0,1,0))
while q:
    value,idx,jump=q.pop()
    dp[idx]=min(dp[idx],value)
    for i in range(3):
        nx=jump+dx[i]
        if idx+nx==n:
            print(value+1)
            exit()
        if idx+nx>n or dp[idx+nx]==-1 or nx<=0 or nx in visited[idx+nx]:
            continue
        visited[idx+nx].append(nx)
        q.appendleft((value+1,idx+nx,nx))


print(-1)