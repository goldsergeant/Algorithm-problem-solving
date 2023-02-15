import sys

n,m=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
answer=0
for one in range(len(cards)-2):
    for two in range(one+1,len(cards)-1):
        for three in range(two+1,len(cards)):
            if cards[one]+cards[two]+cards[three]<=m:
                answer=max(answer,cards[one]+cards[two]+cards[three])

print(answer)