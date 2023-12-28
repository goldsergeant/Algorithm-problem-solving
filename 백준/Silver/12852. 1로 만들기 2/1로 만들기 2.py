import collections
import sys

N=int(sys.stdin.readline())
answer=[]
visited=[False]*(N+1)
q=collections.deque([(1,[1])])
visited[1]=True
while q:
    num,visited_nums=q.popleft()
    if num==N:
        print(len(visited_nums)-1)
        print(*reversed(visited_nums))
        break

    if num*3<=N and not visited[num*3]:
        visited[num*3]=True
        q.append((num*3,visited_nums+[num*3]))
    if num*2<=N and not visited[num*2]:
        visited[num*2]=True
        q.append((num*2,visited_nums+[num*2]))
    if num+1<=N and not visited[num+1]:
        visited[num+1]=True
        q.append((num+1,visited_nums+[num+1]))


