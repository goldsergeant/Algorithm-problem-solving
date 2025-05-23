import sys


def dfs(idx, last, cnt, total):
    if idx == N:
        return total*people[idx]
    if dp[idx][last][cnt] != sys.maxsize:
        return dp[idx][last][cnt]

    if cnt < M:
        dp[idx][last][cnt] = min(dp[idx][last][cnt], dfs(idx + 1, idx, cnt + 1, 0))  #현재 방 청소하는 경우

    dp[idx][last][cnt] = min(dp[idx][last][cnt],
                              dfs(idx + 1, last, cnt, total + people[idx]))  #현재 방 청소안하는 경우

    dp[idx][last][cnt]+=total*people[idx]

    return dp[idx][last][cnt]


N, M = map(int, sys.stdin.readline().split())
people = [0]+list(map(int, sys.stdin.readline().split()))
dp = [[[sys.maxsize for _ in range(M + 1)] for _ in range(N+1)] for _ in range(N+1)]  # 현재 방, 마지막 청소한 방, 방 청소 횟수

print(dfs(1, 0, 0, 0))

cnt = 0
prev = 0
answer = []
for i in range(1,N+1):
    if cnt == M:
        break
    if dp[i+1][prev][cnt]>=dp[i+1][i][cnt+1]:
        answer.append(i)
        prev=i
        cnt+=1
print(*answer)