import sys
from heapq import heappush,heappop

N=int(sys.stdin.readline())
homeworks=[]
answer=0
for _ in range(N):
    deadline,ramen_cnt=map(int,sys.stdin.readline().split())
    homeworks.append((deadline,ramen_cnt))

homeworks.sort(key=lambda x:(x[0],-x[1]))

q=[]
for deadline,ramen_cnt in homeworks:
    if len(q)<deadline:
        heappush(q,ramen_cnt)
    elif len(q)==deadline and q[0]<ramen_cnt:
        heappop(q)
        heappush(q,ramen_cnt)

print(sum(q))



