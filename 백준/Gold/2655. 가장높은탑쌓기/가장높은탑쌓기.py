import sys
from functools import cache

@cache
def dfs(idx):

    tmp=bricks[idx][1]
    for i in range(N):
        if idx==i:
            continue

        if bricks[idx][0]>bricks[i][0] and bricks[idx][2]>bricks[i][2]:
            if tmp<bricks[idx][1]+dfs(i):
                tmp=bricks[idx][1]+dfs(i)
                next_brick[idx]=i

    return tmp



N=int(sys.stdin.readline())
bricks=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
max_height=0
cur_brick=-1
next_brick=[-1 for _ in range(N)]
for i in range(N):
    if dfs(i)>max_height:
        max_height=dfs(i)
        cur_brick=i
max_bricks=[]
while cur_brick!=-1:
    max_bricks.append(cur_brick)
    cur_brick=next_brick[cur_brick]

print(len(max_bricks))
print(*map(lambda x:x+1,max_bricks[::-1]),sep='\n')