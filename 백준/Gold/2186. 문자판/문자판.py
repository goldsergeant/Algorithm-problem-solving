import collections
import sys

N, M, K = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
target = sys.stdin.readline().rstrip()
answer=0
dp=[[[-1 for _ in range(len(target))] for _ in range(M)] for _ in range(N)]

def dfs(r,c,word_idx):
    if dp[r][c][word_idx]!=-1:
        return dp[r][c][word_idx]
    if word_idx==len(target)-1:
        return 1

    dp[r][c][word_idx]=0
    for k in range(1, K + 1):
        for dy, dx in [(-1 * k, 0), (1 * k, 0), (0, -1 * k), (0, 1 * k)]:
            n_r, n_c = r + dy, c + dx
            if 0 <= n_r < N and 0 <= n_c < M:
                if board[n_r][n_c] == target[word_idx+1]:
                    dp[r][c][word_idx]+=dfs(n_r, n_c, word_idx + 1)

    return dp[r][c][word_idx]

for i in range(N):
    for j in range(M):
        if board[i][j]==target[0]:
            answer+=dfs(i,j,0)

print(answer)