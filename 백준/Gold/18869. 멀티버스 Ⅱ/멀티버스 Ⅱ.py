import sys
from itertools import combinations

M, N = map(int, sys.stdin.readline().split())
answer = 0
spaces=[]
for _ in range(M):
    arr=dict((x,True) for x in map(int,sys.stdin.readline().split())).keys()
    space={idx:u for idx,u in enumerate(arr)}
    space=sorted(space,key=space.get)
    spaces.append(tuple(space))

for space1,space2 in combinations(spaces,2):
    if space1==space2:
        answer+=1

print(answer)
