import sys

N=int(sys.stdin.readline())
assignments=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
assignments.sort(key=lambda x:x[1],reverse=True)
visited_day=[False for _ in range(1000+1)]

score=0
for i in range(N):
    if not visited_day[assignments[i][0]]:
        visited_day[assignments[i][0]]=True
        score+=assignments[i][1]
    else:
        cur=assignments[i][0]
        while cur>=1 and visited_day[cur]:
            cur-=1
        if cur>=1 and not visited_day[cur]:
            visited_day[cur]=True
            score+=assignments[i][1]

print(score)