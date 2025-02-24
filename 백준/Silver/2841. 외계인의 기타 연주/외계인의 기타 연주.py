import sys

N,P=map(int,sys.stdin.readline().split())
stacks=[[] for _ in range(N+1)]
answer=0
for _ in range(N):
    line,pret=map(int,sys.stdin.readline().split())
    while stacks[line] and stacks[line][-1]>pret:
        stacks[line].pop()
        answer+=1

    if stacks[line] and stacks[line][-1]==pret:
        continue
    else:
        answer+=1
        stacks[line].append(pret)

print(answer)