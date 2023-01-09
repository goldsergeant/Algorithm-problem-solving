import sys

n,m=map(int,sys.stdin.readline().split())
board=[]
answer=sys.maxsize
for i in range(n):
    board.append(sys.stdin.readline().rstrip())

for y in range(n-7):
    for x in range(m-7):
        start_black=0
        start_white=0
        for i in range(y,y+8):
            for j in range(x,x+8):
                if (i+j)%2==0:
                    if board[i][j]=='B':
                        start_white+=1
                    elif board[i][j]=='W':
                        start_black+=1
                elif (i+j)%2==1:
                    if board[i][j]=='B':
                        start_black+=1
                    elif board[i][j]=='W':
                        start_white+=1
        answer=min(answer,start_white,start_black)
print(answer)