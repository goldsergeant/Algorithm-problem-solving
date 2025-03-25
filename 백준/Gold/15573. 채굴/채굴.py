import collections
import sys

def bfs(s_r,s_c,st):
    visited[s_r][s_c]=True
    q=collections.deque([(s_r,s_c)])
    cnt=0
    while q:
        r,c=q.popleft()
        cnt+=1

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and strengths[nr][nc]<=st:
                visited[nr][nc]=True
                q.append((nr,nc))

    return cnt

def check(mid):
    cnt=0
    for i in range(N):
        if not visited[i][0] and strengths[i][0] <= mid:
            cnt+= bfs(i, 0, mid)
        if not visited[i][M - 1] and strengths[i][M - 1] <= mid:
            cnt+= bfs(i,M-1,mid)

    for j in range(M):
        if not visited[0][j] and strengths[0][j] <= mid:
            cnt+=bfs(0,j,mid)

    return cnt>=K

N,M,K=map(int,sys.stdin.readline().split())
strengths=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=sys.maxsize
left,right=1,10**6

while left+1<right:
    mid = (left+right)//2
    visited = [[False for _ in range(M)] for _ in range(N)]
    if check(mid):
        right=mid
    else:
        left=mid

print(right)