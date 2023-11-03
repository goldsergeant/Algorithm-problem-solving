import collections
import sys

n,x=map(int,sys.stdin.readline().split())
flavor_arr=list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
flavor_arr.sort(key=lambda x:(x[0]-x[1]),reverse=True)
answer=0

for idx,(a,b) in enumerate(flavor_arr):
    if a>b and x>=(5000+(len(flavor_arr)-(idx+1))*1000):
        answer+=a
        x-=5000
    else:
        answer+=b
        x-=1000

print(answer)


