import sys

sys.setrecursionlimit(100000)


def solution(land, height):
    def dfs(r, c, num):
        zone[r][c] = num
        for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0),:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(land) and 0 <= nc < len(land) and zone[nr][nc] == 0 and abs(
                    land[r][c] - land[nr][nc]) <= height:
                dfs(nr, nc, num)

    def find(x):
        if parent_zone[x]!=x:
            parent_zone[x]=find(parent_zone[x])
        return parent_zone[x]

    def union(a,b):
        a=find(a)
        b=find(b)
        if a>b:
            parent_zone[a]=b
        else:
            parent_zone[b]=a


    zone = [[0 for _ in range(len(land))] for _ in range(len(land))]
    edges = []
    cur = 1
    answer=0
    for i in range(len(land)):
        for j in range(len(land)):
            if zone[i][j] == 0:
                dfs(i, j, cur)
                cur += 1

    parent_zone=[i for i in range(cur)]

    for i in range(len(land)):
        for j in range(len(land)):
            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0),:
                nr, nc = i + dr, j + dc
                if 0 <= nr < len(land) and 0 <= nc < len(land) and zone[i][j] != zone[nr][nc]:
                    points = sorted([(nr, nc), (i, j)])
                    r1, c1 = points[0]
                    r2, c2 = points[1]
                    edges.append((r1, c1, r2, c2, abs(land[i][j] - land[nr][nc])))

    edges.sort(key=lambda x:x[4])

    for r1,c1,r2,c2,cost in edges:
        a_zone=zone[r1][c1]
        b_zone=zone[r2][c2]
        if find(a_zone)!=find(b_zone):
            union(a_zone,b_zone)
            answer+=cost
    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))