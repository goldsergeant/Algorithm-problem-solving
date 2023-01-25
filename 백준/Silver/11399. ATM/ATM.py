import sys

n=int(input())
p=list(map(int,sys.stdin.readline().split()))
p.sort()
answer=0
for i in range(len(p)):
    answer+=sum(p[0:i+1])

print(answer)