import sys


def find(r, c):
    if (r, c) != parent[r][c]:
        parent[r][c]= find(*parent[r][c])
    return parent[r][c]

def union(r1,c1,r2,c2):
    r1,c1=find(r1,c1)
    r2,c2=find(r2,c2)
    if r1<r2:
        parent[r2][c2]=(r1,c1)
    elif r1>r2:
        parent[r1][c1]=(r2,c2)
    else:
        if c1<c2:
            parent[r2][c2]=(r1,c1)
        else:
            parent[r1][c1]=(r2,c2)


T = int(sys.stdin.readline())
for _ in range(T):
    R, C = map(int, sys.stdin.readline().split())
    parent = [[(i,j) for j in range(C+1)] for i in range(R+1)]
    answer=0
    edges = []
    for r in range(R):
        costs = [*map(int, sys.stdin.readline().split())]
        for c in range(len(costs)):
            edges.append((r+1, c+1, r+1, c + 2, costs[c]))

    for r in range(R - 1):
        costs = [*map(int, sys.stdin.readline().split())]
        for c in range(len(costs)):
            edges.append((r+1, c+1, r + 2, c+1, costs[c]))

    edges.sort(key=lambda x: x[4])
    for s_r, s_c, e_r, e_c, cost in edges:
        s_r,s_c = find(s_r,s_c)
        e_r,e_c = find(e_r,e_c)
        if (s_r,s_c)!=(e_r,e_c):
            union(s_r,s_c,e_r,e_c)
            answer+=cost

    print(answer)
