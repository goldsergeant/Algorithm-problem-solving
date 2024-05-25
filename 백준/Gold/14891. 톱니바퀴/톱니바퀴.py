import sys
from collections import deque

def get_possible(gears,num):
    possible=[False for _ in range(len(gears))]
    possible[num]=True
    for i in range(num-1,-1,-1):
        if gears[i][2]!=gears[i+1][6] and possible[i+1]:
            possible[i]=True

    for i in range(num+1,len(gears)):
        if gears[i-1][2]!=gears[i][6] and possible[i-1]:
            possible[i]=True

    return possible

gears=[deque(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(4)]
K=int(sys.stdin.readline())
for _ in range(K):
    num,dir=map(int,sys.stdin.readline().split())
    num-=1
    tmp=dir
    possible=get_possible(gears,num)

    gears[num].rotate(dir)
    dir=-tmp
    for i in range(num-1,-1,-1):
        if possible[i]:
            gears[i].rotate(dir)
            dir*=-1
        else:
            break

    dir=-tmp

    for i in range(num+1,len(gears)):
        if possible[i]:
            gears[i].rotate(dir)
            dir*=-1
        else:
            break
score=0
for i in range(len(gears)):
    if gears[i][0]:
        score+=2**i

print(score)