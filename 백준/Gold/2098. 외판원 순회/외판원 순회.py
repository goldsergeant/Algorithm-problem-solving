import sys

def dfs(cur,visit_bit):
    if visit_bit==(1<<N)-1: # 전부 방문
        if distance[cur][0]==0:
            return sys.maxsize
        return distance[cur][0]
    if dp[cur][visit_bit]!=-1:
        return dp[cur][visit_bit]
    dp[cur][visit_bit]=sys.maxsize

    for i in range(N):
        if distance[cur][i]==0:
            continue
        if visit_bit&(1<<i)==(1<<i): # 방문 체크
            continue
        dp[cur][visit_bit]=min(dp[cur][visit_bit],dfs(i,visit_bit|(1<<i))+distance[cur][i])

    return dp[cur][visit_bit]

N = int(sys.stdin.readline())
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(1<<N)] for _ in range(N)] # 마지막 노드, 합산한 비트
print(dfs(0,1))