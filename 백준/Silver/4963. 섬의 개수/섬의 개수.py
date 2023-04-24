import sys
sys.setrecursionlimit(10000)

dx=[0,0,1,-1,1,-1,1,-1]
dy=[1,-1,0,0,1,-1,-1,1]


def dfs(w, h, i, j, land):
    for idx in range(8):
        nx = j + dx[idx]
        ny = i + dy[idx]
        if nx < 0 or ny < 0 or nx > w - 1 or ny > h - 1:
            continue
        if land[ny][nx]==1:
            land[ny][nx]=0
            dfs(w,h,ny, nx,land)

def solve():
    while True:
        w,h=map(int,sys.stdin.readline().split())
        land=[]
        answer=0

        if w==0 and h==0:
            break
        for _ in range(h):
            land.append(list(map(int,sys.stdin.readline().split())))


        for i in range(h):
            for j in range(w):
                if land[i][j]==1:
                    land[i][j]=0
                    dfs(w,h,i,j,land)
                    answer+=1
        print(answer)

solve()