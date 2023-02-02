import collections
import sys

n=int(input())
deq=collections.deque()
for i in range(n):
    s=sys.stdin.readline()
    s=s.strip()
    if 'push_back' in s or 'push_front' in s:
        a,b=s.split()
        if a=='push_back':
            deq.append(b)
        else:
            deq.appendleft(b)
    elif s=='front':
        print(deq[0] if len(deq)>0 else -1)
    elif s=='back':
        print(deq[-1] if len(deq)>0 else -1)
    elif s=='size':
        print(len(deq))
    elif s=='empty':
        print(1 if len(deq)==0 else 0)
    elif s=='pop_front':
        print(deq.popleft() if len(deq)>0 else -1)
    elif s=='pop_back':
        print(deq.pop() if len(deq)>0 else -1)
