import collections
import itertools
import sys

board = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
combs=list(itertools.combinations([(i,j) for i in range(5) for j in range(5)],7))

def is_adjacented(arr):
    q=collections.deque([arr[0]])
    visited=[False]*7
    visited[0]=True

    while q:
        y,x=q.popleft()

        for i in range(4):
            ny=dy[i]+y
            nx=dx[i]+x
            if (ny,nx) in arr:
                next_idx=arr.index((ny,nx))
                if not visited[next_idx]:
                    visited[next_idx]=True
                    q.append((ny,nx))
    return all(visited)

def many_dasom(arr):
    dasom=0
    for y,x in arr:
        if board[y][x]=='S':
            dasom+=1

    return dasom>=4

print(len(list(filter(lambda x:many_dasom(x) and is_adjacented(x),combs))))


