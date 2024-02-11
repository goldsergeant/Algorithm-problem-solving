import collections
import sys

T,A,B=map(int,sys.stdin.readline().split())
def bfs():
    q=collections.deque([(0,0)])
    visited = [[False for _ in range(2)] for _ in range(T + 1)]
    visited[0][0]=True

    max_node=0
    while q:
        cur,is_used=q.popleft()
        max_node=max(max_node,cur)

        for full in (A,B):
            if cur+full<=T and not visited[cur+full][is_used]:
                visited[cur+full][is_used]=True
                q.append((cur+full,is_used))
        if not is_used and not visited[cur//2][True]:
            visited[cur//2][True]=True
            q.append((cur//2,True))

    return max_node

print(bfs())