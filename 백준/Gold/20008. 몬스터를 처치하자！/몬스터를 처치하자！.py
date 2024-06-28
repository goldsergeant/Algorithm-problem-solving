import sys

def dfs(time,hp,cool):
    global answer
    if hp<=0:
        answer=min(answer,time)
        return

    flag=False
    for i in range(N):
        if cool[i]+skills[i][0]>time:
            continue

        tmp=cool[:]
        tmp[i]=time
        dfs(time+1,hp-skills[i][1],tmp)
        flag=True

    if not flag:
        dfs(time+1,hp,cool)




N,HP=map(int,sys.stdin.readline().split())
skills=[[*map(int,sys.stdin.readline().split())] for _ in range(N)]
answer=sys.maxsize
dfs(0,HP,[-sys.maxsize for _ in range(N)])
print(answer)