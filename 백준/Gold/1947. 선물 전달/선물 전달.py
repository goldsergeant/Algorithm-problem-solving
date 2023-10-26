import sys

n=int(sys.stdin.readline())
if n==1:
    print(0)
    exit()
elif n==2:
    print(1)
    exit()

mod_num=1000000000
a=0
b=1
c=0
for i in range(3,n+1):
    c=((i-1)*(a+b))%mod_num
    a,b=b,c

print(c)