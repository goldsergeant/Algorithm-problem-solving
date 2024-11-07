import math
import sys
from functools import cache

input = sys.stdin.readline

# 맨하탄 거리
def get_dist(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
nodes=[[] for _ in range(8+1)]
nodes[1]=[xs,ys]
nodes[8]=[xe,ye]
distance=[[sys.maxsize for _ in range(8+1)] for _ in range(8+1)]

idx=2
for _ in range(1,3+1):
    x1, y1, x2, y2 = map(int, input().split())
    nodes[idx]=[x1,y1]
    nodes[idx+1]=[x2,y2]
    distance[idx][idx+1]=10
    distance[idx+1][idx]=10
    idx+=2

for i in range(1,8+1):
    for j in range(1,8+1):
        a=nodes[i]
        b=nodes[j]
        distance[i][j]=min(distance[i][j],get_dist(a[0],a[1],b[0],b[1]))

for k in range(1,8+1):
    for i in range(1,8+1):
        for j in range(1,8+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

print(distance[1][8])