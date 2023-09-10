import collections
import sys

n,q=map(int,input().split())
logs=[0]+[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
questions=[list(map(int,sys.stdin.readline().split())) for _ in range(q)]

def bfs(question)->int:
    start,target=question
    queue=collections.deque()
    queue.appendleft(start)
    visited=[False for _ in range(n+1)]
    visited[start]=True

    while queue:
        cur=queue.pop()
        x1,x2,y=logs[cur]

        for i in range(1,len(logs)):
            new_x1,new_x2,new_y=logs[i]
            if not visited[i]:
                if new_x1<=x1<=new_x2 or new_x1<=x2<=new_x2:
                    if i==target:
                        return 1
                    visited[i]=True
                    queue.appendleft(i)

    return 0

for question in questions:
    print(bfs(question))