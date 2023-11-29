import sys

n=int(sys.stdin.readline())
flavors=list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
answer=sys.maxsize
def dfs(idx,sin,ssu):
    global answer
    answer=min(answer,abs(sin-ssu))

    for i in range(idx+1,n):
        dfs(i,sin*flavors[i][0],ssu+flavors[i][1])

for i in range(n):
    dfs(i,flavors[i][0],flavors[i][1])
print(answer)