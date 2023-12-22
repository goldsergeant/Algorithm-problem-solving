import sys

N=int(sys.stdin.readline())
scores=list(map(int,sys.stdin.readline().split()))
print(sum(map(lambda x:x/max(scores)*100,scores))/N)