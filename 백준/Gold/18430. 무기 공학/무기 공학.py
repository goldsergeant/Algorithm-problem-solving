import sys

dy_arr = [(-1, 0), (0, -1), (0, 1), (1, 0)]
dx_arr = [(0, 1), (-1, 0), (-1, 0), (0, 1)]

N, M = map(int, sys.stdin.readline().split())
strength = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0


def check(r, c, dy, dx):
    if visited[r][c]:
        return False
    for i in range(2):
        ny, nx = r + dy[i], c + dx[i]
        if ny < 0 or ny > N - 1 or nx < 0 or nx > M - 1 or visited[ny][nx]:
            return False
    return True


def get_boomerang(r, c, dy, dx):
    total = strength[r][c] * 2
    for i in range(2):
        nr, nc = r + dy[i], c + dx[i]
        total += strength[nr][nc]
    return total


def dfs(r, c, total):
    global answer
    if c == M:
        c = 0
        r += 1
    if r == N:
        answer = max(answer, total)
        return

    for i in range(len(dy_arr)):
        if check(r, c, dy_arr[i], dx_arr[i]):
            visited[r][c] = True
            for j in range(2):
                ny, nx = r + dy_arr[i][j], c + dx_arr[i][j]
                visited[ny][nx] = True

            dfs(r, c + 1, total + get_boomerang(r, c, dy_arr[i], dx_arr[i]))

            visited[r][c] = False
            for j in range(2):
                ny, nx = r + dy_arr[i][j], c + dx_arr[i][j]
                visited[ny][nx] = False

    dfs(r, c + 1, total)


dfs(0, 0, 0)
print(answer)
