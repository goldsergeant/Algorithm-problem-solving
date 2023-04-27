import collections
import sys

N,K=map(int,sys.stdin.readline().split())
path=[]
def bfs():
    queue=collections.deque()
    visited=[-1 for _ in range(100001)]
    queue.append((N,0,[N]))
    visited[N]=True

    while queue:
        node=queue.popleft()
        cur,depth=node[0],node[1]

        if cur==K:
            print(depth)
            idx=cur
            while idx!=N:
                path.append(idx)
                idx=visited[idx]
            path.append(N)
            print(*path[::-1])
            break

        if cur-1>=0 and visited[cur-1]==-1:
            visited[cur-1]=cur
            queue.append((cur-1,depth+1))

        if cur<K and visited[cur+1]==-1:
            visited[cur+1]=cur
            queue.append((cur+1,depth+1))

        if 2*cur<100001 and cur<K and visited[2*cur]==-1:
            visited[2*cur]=cur
            queue.append((2*cur,depth+1))

bfs()