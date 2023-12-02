import sys

max_num=123456*2
is_prime=[True]*(max_num+1)
is_prime[1]=False
is_prime[2]=True
for i in range(2,max_num+1):
    if is_prime[i]:
        for j in range(2*i,max_num+1,i):
            is_prime[j]=False

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break

    print(len(list(filter(lambda x:x==True,is_prime[n+1:2*n+1]))))