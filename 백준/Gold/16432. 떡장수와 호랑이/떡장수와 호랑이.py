import sys
sys.setrecursionlimit(100000)

N=int(sys.stdin.readline())
dducks=[]
dp=[]
answer=[]
for _ in range(N):
    inp=list(map(int,sys.stdin.readline().split()))
    m=inp[0]
    dducks.append(inp[1:])
    dp.append([0 for _ in range(m)])

def dfs(day,idx,step):
    if day==N-1:
        answer.append(step)
        return dducks[day][idx]
    if dp[day][idx]!=0:
        return dp[day][idx]

    dp[day][idx]=-1
    for i in range(len(dp[day+1])):
        if dducks[day+1][i]!=dducks[day][idx]:
            dp[day][idx]=dfs(day+1,i,step+[dducks[day+1][i]])

    return dp[day][idx]

for i in range(len(dp[0])):
    dfs(0,i,[dducks[0][i]])

print('\n'.join(map(str,answer[0])) if answer else -1)