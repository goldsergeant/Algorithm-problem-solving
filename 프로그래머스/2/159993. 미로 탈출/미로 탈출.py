import collections
import sys


def solution(maps):
    def bfs():
        q = collections.deque([(0, s_r, s_c,0)])
        visited = [[[False,False] for _ in range(len(maps[0]))] for _ in range(len(maps))]
        visited[s_r][s_c][0] = True
        while q:
            cnt, r,c,visited_lever = q.popleft()
            if (r,c) == (e_r,e_c) and visited_lever:
                return cnt
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr,nc=r+dr,c+dc
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]):
                    if maps[nr][nc]=='L':
                        if not visited[nr][nc][True]:
                            visited[nr][nc][True] = True
                            q.append((cnt+1,nr,nc,True))
                    elif maps[nr][nc]!='X':
                        if not visited[nr][nc][visited_lever]:
                            visited[nr][nc][visited_lever]=True
                            q.append((cnt+1,nr,nc,visited_lever))

        return -1

    s_r, s_c, l_r, l_c, e_r, e_c = 0, 0, 0, 0, 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s_r, s_c = i, j
            elif maps[i][j] == 'E':
                e_r, e_c = i, j
            elif maps[i][j] == 'L':
                l_r, l_c = i, j
    return bfs()

