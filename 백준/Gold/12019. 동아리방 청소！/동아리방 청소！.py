import sys

def dfs(now,cnt,pre,total):
    if dp[now][cnt][pre]!=sys.maxsize:
        return dp[now][cnt][pre]
    if now==N:
        return total * people[now]
    tmp=sys.maxsize
    if cnt<M:
        tmp=min(tmp,dfs(now+1,cnt+1,now,0))
    tmp=min(tmp,dfs(now+1,cnt,pre,total+people[now]))
    tmp+=total*people[now]
    dp[now][cnt][pre]=tmp
    return dp[now][cnt][pre]

N,M=map(int,sys.stdin.readline().split())
people=[0]+list(map(int,sys.stdin.readline().split()))
dp=[[[sys.maxsize for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
answer=[]

pre=0
cnt=0


print(dfs(1,0,0,0))
for day in range(1,N):
    if cnt==M:
        break
    if dp[day+1][cnt][pre]>=dp[day+1][cnt+1][day]:
        answer.append(day)
        pre=day
        cnt+=1
print(*answer)