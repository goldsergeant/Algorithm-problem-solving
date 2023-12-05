import math
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    L,N=map(int,sys.stdin.readline().split())
    ant_positions=[]
    for _ in range(N):
        ant_positions.append(int(sys.stdin.readline()))

    min_answer=0
    max_answer=0

    for position in ant_positions:
        min_answer=max(min_answer,min(L-position,position))
        max_answer=max(max_answer,max(L-position,position))

    print(min_answer,max_answer)
