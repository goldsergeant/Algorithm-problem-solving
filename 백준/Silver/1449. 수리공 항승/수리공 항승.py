import sys

N,L=map(int,sys.stdin.readline().split())
tapes=list(map(int,sys.stdin.readline().split()))
tapes.sort()
cur=-sys.maxsize
answer=0
for tape in tapes:
    if cur+L<tape+0.5:
        cur=tape-0.5
        answer+=1

print(answer)