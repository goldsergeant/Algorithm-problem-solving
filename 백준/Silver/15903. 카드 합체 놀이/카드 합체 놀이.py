from heapq import heapify,heappush,heappop
import sys

n,m=map(int, sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
heapify(a)

while m>0:
    x,y=heappop(a),heappop(a),
    heappush(a,x+y)
    heappush(a,x+y)
    m-=1

print(sum(a))