import sys

N=int(sys.stdin.readline())
scores=list(map(int,sys.stdin.readline().split()))
limit_score=int(sys.stdin.readline())
left=-1
right=max(scores)+1

def check(mid):
    return sum([min(mid,scores[i]) for i in range(N)])<=limit_score

while left+1<right:
    mid=(left+right)//2
    if check(mid):
        left=mid
    else:
        right=mid

print(left)