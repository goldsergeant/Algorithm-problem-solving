import sys

def dfs(bit):
    if str(bin(bit)).count('1')>=P:
        return 0
    if dp[bit]!=sys.maxsize:
        return dp[bit]

    for i in range(N):
        if not bit&(1<<i):
            continue
        for j in range(N):
            if bit&(1<<j):
                continue
            dp[bit]=min(dp[bit],dfs(bit|(1<<j))+costs[i][j])

    return dp[bit]

N=int(sys.stdin.readline())
costs=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
on_off=list(sys.stdin.readline().strip())
P=int(sys.stdin.readline())
dp=[sys.maxsize for _ in range(1<<N)]
start_bit=0
for i in range(len(on_off)):
    if on_off[i]=='Y':
        start_bit|=(1<<i)

answer=dfs(start_bit)
print(answer if answer<sys.maxsize else -1)