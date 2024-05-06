import collections
import sys

def bfs():
    visited=[sys.maxsize for _ in range(200000+1)]
    q=collections.deque([(N,0)])
    min_time=sys.maxsize
    cnt=0
    while q:
        cur,time=q.popleft()
        if cur==K:
            if time<min_time:
                cnt=1
                min_time=time
            elif time==min_time:
                cnt+=1
            continue
        for next_spot in [cur-1,cur+1,cur*2]:
            if 0<=next_spot<=200000 and visited[next_spot]>=time+1:
                visited[next_spot]=time+1
                q.append((next_spot,time+1))

    return min_time,cnt


N,K=map(int,sys.stdin.readline().split())
print(*bfs(),sep='\n')