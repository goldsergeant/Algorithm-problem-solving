import sys

k,n=map(int,sys.stdin.readline().split())
lines=[]
for _ in range(k):
    lines.append(int(input()))

mini=1
maxi=max(lines)
answer=0
while mini<=maxi:
    mid=(mini+maxi)//2
    count=0
    for line in lines:
        count+=line//mid
    if count>=n:
        mini=mid+1
    elif count<n:
        maxi=mid-1
print(maxi)