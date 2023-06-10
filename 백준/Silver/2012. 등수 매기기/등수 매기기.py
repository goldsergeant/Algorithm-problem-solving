import sys

n=int(input())
rank=[]
answer=0
for _ in range(n):
    rank.append(int(sys.stdin.readline().rstrip()))

rank.sort()
for i in range(1,n+1):
    answer+=abs(rank[i-1]-i)

print(answer)