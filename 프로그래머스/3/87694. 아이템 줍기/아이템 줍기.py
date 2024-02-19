import collections
import sys


def solution(rectangle, characterX, characterY, itemX, itemY):

    def is_border(s_r, s_c):
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]:
            ny = s_r + dy
            nx = s_c + dx
            if not board[ny][nx]:
                return True
        return False

    board = [[0 for _ in range((50 + 1)*2)] for _ in range((50 + 1)*2)]
    visited1 = [[sys.maxsize for _ in range((50 + 1)*2)] for _ in range((50 + 1)*2)]
    border_points = []
    for r in rectangle:
        lbx, lby, rtx, rty=map(lambda x:x*2,r)
        for y in range(lby, rty + 1):
            for x in range(lbx, rtx + 1):
                board[y][x] = 1

    for y in range(1, (50 + 1)*2):
        for x in range(1, (50 + 1)*2):
            if board[y][x] and not is_border(y, x):
                border_points.append((y, x))

    for y, x in border_points:
        board[y][x] = 0

    def bfs2(s_r, s_c):
        q = collections.deque([(s_r, s_c)])
        visited1[s_r][s_c] = 0

        while q:
            r, c = q.popleft()
            if r == itemY*2 and c == itemX*2:
                return visited1[r][c] // 2

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny = r + dy
                nx = c + dx
                if board[ny][nx] and visited1[r][c] + 1 < visited1[ny][nx]:
                    visited1[ny][nx] = visited1[r][c] + 1
                    q.append((ny, nx))


    return bfs2(characterY*2,characterX*2)


