import collections
import sys

one, two, three = map(int, sys.stdin.readline().split())
total = one + two + three


def bfs():
    visited = [[False for _ in range(500*3+1)] for _ in range(500*3+1)]
    q = collections.deque()
    q.append((max(one,two,three),min(one,two,three)))
    visited[max(one,two,three)][min(one,two,three)]=True

    while q:
        a, b = q.popleft()
        c = total - (a + b)
        if a == b == c:
            return 1

        for x,y in (a,b),(a,c),(b,c):
            if x!=y:
                x,y=max(x,y),min(x,y)
                x -= y
                y *= 2
                z=total-(x+y)

                maxi,mini=max(x, y,z),min(x, y,z)
                if not visited[maxi][mini]:
                    visited[maxi][mini] = True
                    q.append((maxi, mini))

    return 0


print(bfs())
