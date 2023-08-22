import math
import sys

paper=dict()
answer=0
for i in range(1,7):
    paper[i]=int(sys.stdin.readline())

answer+=paper[6]
paper[6]=0

while paper[5]>0:
    area=36-25
    paper[5]-=1
    paper[1]=max(0,paper[1]-area)
    answer+=1

while paper[4]>0:
    area=36-16
    area-=min(paper[2],5)*4
    paper[4]-=1
    paper[2]=max(0,paper[2]-5)
    paper[1]=max(0,paper[1]-area)
    answer+=1

while paper[3]>0:
    area=36-9*min(paper[3],4)
    if paper[3]>=4:
        paper[3]-=4
        area=0
    elif paper[3]==3:
        paper[3]-=3
        area-=min(paper[2],1)*4
        paper[2]=max(0,paper[2]-1)
    elif paper[3]==2:
        paper[3]-=2
        area-=min(paper[2],3)*4
        paper[2]=max(0,paper[2]-3)

    elif paper[3]==1:
        paper[3]-=1
        area-=min(paper[2],5)*4
        paper[2]=max(0,paper[2]-5)
        
    paper[1]=max(0,paper[1]-area)
    answer+=1

while paper[2]>0:
    area=36-min(paper[2],9)*4
    paper[2]=max(0,paper[2]-9)
    paper[1]=max(0,paper[1]-area)

    answer+=1

while paper[1]>0:
    paper[1]=max(0,paper[1]-36)

    answer+=1

print(answer)