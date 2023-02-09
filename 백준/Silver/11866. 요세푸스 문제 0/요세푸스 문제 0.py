import sys

n,k=map(int,sys.stdin.readline().split())
people=[i for i in range(1,n+1)]
answer=[]
cur=0
for _ in range(n):
    cur+=k-1
    if cur>=len(people):
        cur%=len(people)
    answer.append(people.pop(cur))

print('<'+', '.join(map(str,answer))+'>')