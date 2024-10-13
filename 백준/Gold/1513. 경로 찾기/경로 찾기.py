import collections
import sys

MOD_NUM = 1000007

N, M, C = map(int, sys.stdin.readline().split())
dp = [[[[0 for _ in range(C + 1)] for _ in range(C + 1)] for _ in range(M + 1)] for _ in range(N + 1)]  ## r,c,최대숫자,방문횟수
game_zone_num = collections.defaultdict(int)
for i in range(1, C + 1):
    r, c = map(int, sys.stdin.readline().split())
    game_zone_num[(r, c)] = i

if game_zone_num[(1, 1)] == 0:
    dp[1][1][0][0] = 1
else:
    dp[1][1][game_zone_num[(1, 1)]][1] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 and j == 1:
            continue

        if game_zone_num[(i, j)] == 0:  # 오락실이 아닐경우
            for k in range(C+1):
                for l in range(k+1):
                    dp[i][j][k][l]+=(dp[i-1][j][k][l]+dp[i][j-1][k][l])%MOD_NUM
        else:  # 오락실일 경우
            game_num=game_zone_num[(i, j)]
            for k in range(game_num):
                for l in range(game_num):
                    dp[i][j][game_num][l+1]+=(dp[i-1][j][k][l]+dp[i][j-1][k][l])%MOD_NUM

answer=[0 for _ in range(C+1)]
for i in range(C+1):
    for j in range(C+1):
        answer[i]=(answer[i]+dp[N][M][j][i])%MOD_NUM
print(*answer)