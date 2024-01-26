import sys
from math import ceil

MONSTER=1
PORTION=2

N,H=map(int,sys.stdin.readline().split())
rooms=[[]]
for i in range(N):
    t,a,h=map(int,sys.stdin.readline().split())
    rooms.append((t,a,h))

total_damage=0
need_hp=0
for i in range(1,N+1):
    t,a,h=rooms[i]
    if t==MONSTER:
        total_damage+=(ceil(h/H)-1)*a
        need_hp=max(need_hp,total_damage)
    elif t==PORTION:
        total_damage=max(0,total_damage-h)
        H+=a

need_hp+=1
print(need_hp)