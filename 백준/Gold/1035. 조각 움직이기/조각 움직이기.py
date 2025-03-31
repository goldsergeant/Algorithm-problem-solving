import collections
import sys

def check(arr):
    vis=set()
    q=collections.deque()
    q.append((arr[0][0], arr[0][1]))
    vis.add((arr[0][0], arr[0][1]))
    cnt=0
    while q:
        r,c=q.popleft()
        cnt+=1
        for dr,dc in (0,1),(0,-1),(1,0),(-1,0):
            nr,nc=r+dr,c+dc
            if 0<=nr<5 and 0<=nc<5 and (nr,nc) in arr and (nr, nc) not in vis:
                vis.add((nr,nc))
                q.append((nr,nc))

    return cnt==piece_count

def get_pieces_count():
    cnt=0
    for i in range(5):
        for j in range(5):
            if board[i][j]=='*':
                cnt+=1
    return cnt

def bfs():
    visited=set()
    init_arr=[]
    q=collections.deque()
    for i in range(5):
        for j in range(5):
            if board[i][j]=='*':
                init_arr.append((i,j))

    visited.add(tuple(init_arr))
    q.append(init_arr)
    move_cnt=0
    while q:
        for _ in range(len(q)):
            if check(q[0]):
                return move_cnt

            arr = q.popleft()
            for i in range(len(arr)):
                for dr,dc in (0,1),(0,-1),(1,0),(-1,0):
                    nr,nc=arr[i][0]+dr,arr[i][1]+dc
                    if 0<=nr<5 and 0<=nc<5:
                        next_arr=arr[:i]+[(nr,nc)]+arr[i+1:]
                        next_tup=tuple(sorted(next_arr))
                        if next_tup not in visited and (nr,nc) not in arr:
                            visited.add(next_tup)
                            q.append(next_arr)
        move_cnt+=1


board=[list(sys.stdin.readline().strip()) for _ in range(5)]
piece_count=get_pieces_count()
print(bfs())