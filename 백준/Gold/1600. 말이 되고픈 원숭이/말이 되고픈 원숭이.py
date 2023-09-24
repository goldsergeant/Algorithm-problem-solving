import collections
import sys

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
horse_move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
normal_move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
q = collections.deque()
q.append((0, 0, 0, 0))
visited=[[[False for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
for i in range(k+1):
    visited[0][0][i]=True

while q:
    cur_row, cur_col, used_chance, step_cnt = q.popleft()
    if cur_row == h - 1 and cur_col == w - 1:
        print(step_cnt)
        sys.exit()

    if used_chance < k:
        for move in horse_move:
            n_row = cur_row + move[0]
            n_col = cur_col + move[1]
            if n_row < 0 or n_col < 0 or n_row > h - 1 or n_col > w - 1:
                continue
            if board[n_row][n_col]==1:
                continue
            if not visited[n_row][n_col][used_chance+1]:
                for i in range(used_chance+1,k+1):
                    visited[n_row][n_col][i]=True
                q.append((n_row, n_col, used_chance + 1, step_cnt + 1))
    for move in normal_move:
        n_row = cur_row + move[0]
        n_col = cur_col + move[1]
        if n_row < 0 or n_col < 0 or n_row > h - 1 or n_col > w - 1:
            continue
        if board[n_row][n_col]==1:
            continue
        if not visited[n_row][n_col][used_chance]:
            for i in range(used_chance,k+1):
                visited[n_row][n_col][i]=True
            q.append((n_row, n_col, used_chance, step_cnt + 1))

print(-1)
