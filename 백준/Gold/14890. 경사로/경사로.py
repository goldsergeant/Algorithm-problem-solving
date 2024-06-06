import sys

def check(line):
    visited=[False for _ in range(N)]
    for i in range(N-1):
        if line[i]==line[i+1]:
            continue
        if abs(line[i]-line[i+1])>1:
            return False
        if line[i]>line[i+1]:
            if i+L>N-1:
                return False
            for n_i in range(i+1,i+L+1):
                if line[i+1]!=line[n_i] or visited[n_i]:
                    return False
                visited[n_i]=True
        else:
            if (i+1)-L<0:
                return False
            for prev_i in range((i+1)-L,i+1):
                if line[i]!=line[prev_i] or visited[prev_i]:
                    return False
                visited[prev_i]=True

    return True


N,L=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=0
for i in range(N):
    if check(board[i]):
        answer+=1


for j in range(N):
    if check([board[i][j] for i in range(N)]):
        answer+=1

print(answer)