import itertools
import sys

N=int(input())
S=list(map(int,sys.stdin.readline().split()))
sum_set=set()
answer=0
for idx in range(1,N+1):
    combi=list(itertools.combinations(S,idx))
    for i in range(len(combi)):
        s=0
        for j in range(len(combi[i])):
            s+=combi[i][j]
        sum_set.add(s)


for i in range(1,100000*20):
    if i not in sum_set:
        answer=i
        break

print(answer)