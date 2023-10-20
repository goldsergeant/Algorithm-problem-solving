import collections
import sys

n, m, t = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    global answer
    queue = collections.deque()
    visited[0][0][0] = True
    queue.append((0, 0, 0, 0))  # row,col,depth,used_chance,have_chance

    while queue:
        row, col, depth,have_gram = queue.popleft()

        if row == n - 1 and col == m - 1:
            return depth

        for i in range(4):
            n_row = row + dy[i]
            n_col = col + dx[i]
            if n_row < 0 or n_col < 0 or n_row > n - 1 or n_col > m - 1:
                continue

            if board[n_row][n_col] == 0 and not visited[n_row][n_col][have_gram]:
                visited[n_row][n_col][have_gram] = True
                queue.append((n_row, n_col, depth + 1, have_gram))

            elif board[n_row][n_col] == 2 and not visited[n_row][n_col][
                have_gram] and have_gram == 0:
                visited[n_row][n_col][0] = True
                queue.append((n_row, n_col, depth + 1,  1))

            elif board[n_row][n_col] == 1 and have_gram == 1 and not visited[n_row][n_col][1]:
                visited[n_row][n_col][1] = True
                queue.append((n_row, n_col, depth + 1, 1))

answer=bfs()
print(answer if answer and answer<=t else 'Fail')
