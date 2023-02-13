import sys

global white
white=0
global blue
blue=0

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

def dfs(n:int, x,y):
    global white
    global blue
    flag_white=0
    flag_blue=0
    for i in range(y,y+n):
        for j in range(x,x+n):
            if board[i][j]==0:
                flag_white=1
            else:
                flag_blue=1
    if flag_white==1 and flag_blue==1:
        dfs(n//2,x,y) #1번
        dfs(n//2,x+n//2,y) #2번
        dfs(n//2,x,y+n//2) #3번
        dfs(n//2,x+n//2,y+n//2) #4번

    elif flag_white==1 and flag_blue==0:
        white+=1
        return
    elif flag_white==0 and flag_blue==1:
        blue+=1
        return

dfs(n,0,0)
print(white)
print(blue)
