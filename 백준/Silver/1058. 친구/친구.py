import collections
import sys

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
answer=0
for i in range(1,N+1):
    friends=['*']+list(sys.stdin.readline().rstrip())
    for j in range(1,len(friends)):
        if friends[j]=='Y':
            graph[i].append(j)

def bfs(start):
    q=collections.deque([(start,0)])
    friends_cnt=0
    visited=[False]*(N+1)
    visited[start]=True

    while q:
        cur,depth=q.popleft()
        for next in graph[cur]:
            if not visited[next] and depth<2:
                visited[next]=True
                friends_cnt+=1
                q.append((next,depth+1))

    return friends_cnt

for i in range(1,N+1):
    answer=max(answer,bfs(i))

print(answer)
