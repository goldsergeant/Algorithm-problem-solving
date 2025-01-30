import collections
import sys

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = collections.deque([(0, 0, 0, 1)])
    visited[0][0][0] = True

    while q:
        r, c, broken_cnt, cnt = q.popleft()
        is_daytime=cnt%2
        is_waited = False  # 제자리에서 기다렸는가?
        if (r, c) == (N - 1, M - 1):
            return cnt

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if board[nr][nc] == '0':
                if visited[nr][nc][broken_cnt] == 0:
                    q.append((nr, nc, broken_cnt, cnt + 1))
                    visited[nr][nc][broken_cnt] = True
            else:
                if is_daytime:
                    if broken_cnt < K and visited[nr][nc][broken_cnt + 1] == 0:  # 부수고 가는 경우
                        q.append((nr, nc, broken_cnt + 1, cnt + 1))
                        visited[nr][nc][broken_cnt + 1] = True
                else:
                    if not is_waited:
                        q.append((r, c, broken_cnt, cnt + 1))
                        is_waited = True
    return -1


N, M, K = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[[False for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]  # r,c,k
print(bfs())
