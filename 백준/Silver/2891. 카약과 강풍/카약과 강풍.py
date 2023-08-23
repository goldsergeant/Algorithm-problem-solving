import sys

n,s,r=map(int,input().split())
team=[1]*(n+1)
no_kayak=list(map(int,input().split()))
more_kayak=list(map(int,input().split()))
dx=[-1,1]

for num in no_kayak:
    team[num]-=1

for num in more_kayak:
    team[num]+=1

for i in range(1,n+1):
    if team[i]==2:
        for j in range(2):
            nx=i+dx[j]
            if nx<0 or nx>n or team[i]<2:
                continue
            if team[nx]==0:
                team[nx]+=1
                team[i]-=1

print(team.count(0))
