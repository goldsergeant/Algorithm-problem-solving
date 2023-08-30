import collections
import sys

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    answer=0
    mini=sys.maxsize
    for i in range(n):
        l=i+1
        r=n-1
        while l<=r:
            mid=(l+r)//2
            total=s[i]+s[mid]
            if total>k:
                r=mid-1
            else:
                l=mid+1
            if abs(total-k)<mini:
                mini=abs(total-k)
                answer=1
            elif abs(total-k)==mini:
                answer+=1

    print(answer)
