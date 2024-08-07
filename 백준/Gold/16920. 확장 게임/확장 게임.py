import collections
import sys

N,M,P=map(int,sys.stdin.readline().split())
S=[0]+list(map(int,sys.stdin.readline().split()))
board=[list(map(lambda x:int(x) if x.isdigit() else x, sys.stdin.readline().rstrip())) for _ in range(N)]
q_arr=[collections.deque() for _ in range(len(S))]
answer=[0 for _ in range(len(S))]

for i in range(N):
    for j in range(M):
        if type(board[i][j]) is int:
            q_arr[board[i][j]].append((i,j))
            answer[board[i][j]]+=1

flag=True
while flag:
    flag=False
    for idx,q in enumerate(q_arr):
        for _ in range(S[idx]):
            if not q:
                break
            for _ in range(len(q)):
                r,c=q.popleft()

                for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                    nr,nc=r+dr,c+dc
                    if nr<0 or nr>=N or nc<0 or nc>=M or board[nr][nc]!='.':
                        continue
                    board[nr][nc]=idx
                    flag=True
                    answer[idx]+=1
                    q.append((nr,nc))


print(*answer[1:])
#
# for arr in board:
#     print(arr)