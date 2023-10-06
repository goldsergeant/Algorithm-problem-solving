import itertools
import sys

s=list(sys.stdin.readline().rstrip())
answer=set()
for st in itertools.permutations(s,len(s)):
    if all(st[i]!=st[i+1] for i in range(len(s)-1)):
        answer.add(''.join(st))

print(len(answer))