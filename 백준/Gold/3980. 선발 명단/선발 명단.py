import sys

def dfs(idx,total):
    global answer
    if idx==11:
        answer=max(answer,total)
        return

    for i in range(11):
        if board[idx][i]!=0 and not visited[i]:
            visited[i]=True
            dfs(idx+1,total+board[idx][i])
            visited[i]=False

C=int(sys.stdin.readline())
for _ in range(C):
    board=[list(map(int,sys.stdin.readline().split())) for _ in range(11)]
    answer=0
    visited=[False for _ in range(11)]
    dfs(0,0)
    print(answer)