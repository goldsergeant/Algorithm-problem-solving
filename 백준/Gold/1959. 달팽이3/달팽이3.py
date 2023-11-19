import sys

m,n=map(int,sys.stdin.readline().split())
row=col=cnt=0
if m>n:
    cnt=(n-1)*2+1
else:
    cnt=(m-1)*2

if m==n:
    if m%2==0:
        row=m//2+1
        col=n//2
    else:
        row=m//2+1
        col=n//2+1
elif m>n:
    if n%2==0:
        row=n//2+1
        col=n//2
    else:
        row=n//2+1+(m-n)
        col=n//2+1
else:
    if m%2==0:
        row=m//2+1
        col=m//2
    else:
        row=m//2+1
        col=m//2+1+(n-m)


print(cnt)
print(row,col)

