import sys
from collections import deque

N=int(input())
answer=0
chains=deque(sorted(list(map(int,sys.stdin.readline().split()))))

while answer<len(chains)-1:
    chains[0]-=1
    if chains[0]==0:
        chains.popleft()
    answer+=1

print(answer)