import sys

N=int(sys.stdin.readline())
lamps=list(sys.stdin.readline().rstrip())
front_red=[0 for _ in range(N)]
front_green=[0 for _ in range(N)]
front_blue=[0 for _ in range(N)]

for i in range(N):
    if lamps[i]=='R':
        front_red[i],front_green[i],front_blue[i]=0,0,0
    elif lamps[i]=='G':
        front_red[i],front_green[i],front_blue[i]=1,1,1
    else:
        front_red[i],front_green[i],front_blue[i]=2,2,2

tmp_red,tmp_green,tmp_blue=0,0,0
for i in range(N-2):
    if front_red[i]==1:
        for j in range(i,i+3):
            front_red[j]=(front_red[j]+2)%3
        tmp_red+=2
    elif front_red[i]==2:
        for j in range(i,i+3):
            front_red[j]=(front_red[j]+1)%3
        tmp_red+=1

    if front_green[i]==0:
        for j in range(i,i+3):
            front_green[j]=(front_green[j]+1)%3
        tmp_green+=1
    elif front_green[i]==2:
        for j in range(i,i+3):
            front_green[j]=(front_green[j]+2)%3
        tmp_green+=2

    if front_blue[i]==0:
        for j in range(i,i+3):
            front_blue[j]=(front_blue[j]+2)%3
        tmp_blue+=2

    elif front_blue[i]==1:
        for j in range(i,i+3):
            front_blue[j]=(front_blue[j]+1)%3
        tmp_blue+=1

if front_red[N-1]!=0 or front_red[N-2]!=0:
    tmp_red=sys.maxsize
if front_green[N-1]!=1 or front_green[N-2]!=1:
    tmp_green=sys.maxsize
if front_blue[N-1]!=2 or front_blue[N-2]!=2:
    tmp_blue=sys.maxsize

answer=min(tmp_red,tmp_green,tmp_blue)
print(answer if answer!=sys.maxsize else -1)