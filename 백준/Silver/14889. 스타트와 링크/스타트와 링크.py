import sys

n = int(input())
board = []
answer = []
visited=[False for i in range(n)]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


def dfs(start,depth):
    if depth ==n//2:
        s,l=0,0
        for i in range(n-1):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    s+=board[i][j]+board[j][i]
                elif not visited[i] and not visited[j]:
                    l+=board[i][j]+board[j][i]
        answer.append(abs(s-l))
        return

    for i in range(start,n):
        if not visited[i]:
            visited[i]=True
            dfs(i+1,depth+1)
            visited[i]=False

dfs(0,0)
print(min(answer))