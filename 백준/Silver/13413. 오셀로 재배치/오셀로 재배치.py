import collections
import sys

def solve(n,prev,target):
    cnt=[]
    for i in range(n):
        if prev[i]!=target[i]:
            cnt.append(prev[i])

    return cnt.count('B') if cnt.count('B') > cnt.count('W') else cnt.count('W')


t=int(input())
for _ in range(t):
    n=int(sys.stdin.readline().rstrip())
    prev=list(sys.stdin.readline().rstrip())
    target=list(sys.stdin.readline().rstrip())

    print(solve(n,prev,target))

