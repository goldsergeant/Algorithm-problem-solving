import collections
import sys

n,k=map(int,sys.stdin.readline().split())
oasises=list(map(int,sys.stdin.readline().split()))
visited=dict()
dx=[-1,1]
q=collections.deque()
answer=0
for oasis in oasises:
    visited[oasis]=True
    q.appendleft((oasis,0))

while q:
    location,distance=q.pop()
    for i in range(2):
        next_location=location+dx[i]
        if not visited.get(next_location,False):
            visited[next_location]=True
            answer+=distance+1
            k-=1
            q.appendleft((next_location,distance+1))

            if k==0:
                print(answer)
                exit()
