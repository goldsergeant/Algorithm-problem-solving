import collections
import sys


def solution(maps):
    def bfs(x1, y1, x2, y2):
        q = collections.deque([(0, x1, y1)])
        visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[x1][y1] = True
        while q:
            cnt, x, y = q.popleft()
            if (x, y) == (x2, y2):
                return cnt
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((cnt + 1, nx, ny))
        return sys.maxsize

    sx, sy, lx, ly, ex, ey = 0, 0, 0, 0, 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    start_to_lever=bfs(sx, sy, lx, ly)
    if start_to_lever == sys.maxsize:
        return -1
    lever_to_end=bfs(lx,ly,ex,ey)
    if lever_to_end == sys.maxsize:
        return -1
    return start_to_lever+lever_to_end


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))