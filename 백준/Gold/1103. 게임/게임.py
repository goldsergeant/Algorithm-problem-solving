import sys
sys.setrecursionlimit(100000)

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]


visited=[[False for _ in range(M)] for _ in range(N)]

def dfs(y, x):
    if 0 > y or y >= N or 0 > x or x >= M or board[y][x] == 'H':
        return 0

    if visited[y][x]:
        print(-1)
        exit()
    if dp[y][x] != 0:
        return dp[y][x]

    how_many = int(board[y][x])
    visited[y][x]=True
    for dy, dx in (-how_many, 0), (how_many, 0), (0, -how_many), (0, how_many),:
        ny, nx = y + dy, x + dx
        dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)

    visited[y][x]=False

    return dp[y][x]


print(dfs(0, 0))
