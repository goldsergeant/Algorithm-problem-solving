import collections
import sys


def bfs(s_r, s_c):
    global answer
    q = collections.deque([(s_r, s_c)])
    visited[s_r][s_c] = True
    while q:
        r, c = q.popleft()
        if board[r][c] == '$':
            answer += 1
            board[r][c] = '.'
        elif board[r][c].islower():  # 열쇠인 경우
            if board[r][c] not in keys:
                keys.add(board[r][c])
                for nr, nc in door_q[board[r][c].upper()]:
                    if not visited[nr][nc]:
                        q.append((nr, nc))

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if board[nr][nc] == '*':
                    continue
                if visited[nr][nc]:
                    continue
                if board[nr][nc].isupper():
                    if board[nr][nc].lower() not in keys:
                        door_q[board[nr][nc]].append((nr, nc))
                        continue
                visited[nr][nc] = True
                q.append((nr, nc))


T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    board = [['.' for _ in range(w + 2)]] + [['.'] + list(sys.stdin.readline().rstrip())+['.'] for _ in range(h)] + [
        ['.' for _ in range(w + 2)]]
    keys = set(sys.stdin.readline().rstrip())
    door_q = collections.defaultdict(list)
    answer = 0
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    bfs(0, 0)
    print(answer)
