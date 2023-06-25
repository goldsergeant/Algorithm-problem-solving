import collections
import sys

L=int(input())
Ml,Mk=map(int,input().split())
C=int(input())
zombies=[int(sys.stdin.readline().rstrip()) for _ in range(L)]
answer=True

deq=collections.deque()

for i in range(L):
    while deq and deq[0]<=i:
        deq.popleft()

    total_damage=(len(deq)+1)*Mk
    if total_damage>=zombies[i]:
        deq.append(i+Ml)
    elif C>0:
        C-=1
    else:
        answer=False
        break

print('YES' if answer else 'NO')