import sys
from itertools import permutations

A,B=sys.stdin.readline().split()
A=list(A)
B=int(B)
answer=-1

for arr in permutations(A):
    if arr[0]!='0':
        num=int(''.join(arr))
        if num<B:
            answer=max(answer,num)

print(answer)