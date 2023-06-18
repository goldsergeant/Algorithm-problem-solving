import collections
import sys

n=input()
w=list(map(int,input().split()))
answer=sys.maxsize
w.sort()
deq= collections.deque(w)

while deq:
    s1=deq.popleft()
    s2=deq.pop()
    answer=min(answer,s1+s2)

print(answer)