import collections
import sys

col,row=map(int,input().split())
water=list(map(int, input().split()))
if len(water)==1:
    print(0)
    exit()
if col==1 and row==1:
    print(0)
    exit()
answer=0
for i in range(1,len(water)-1):
    l_max,r_max=max(water[:i]),max(water[i+1:])
    if water[i]<l_max and water[i]<r_max:
        answer+=min(l_max,r_max)-water[i]
print(answer)

