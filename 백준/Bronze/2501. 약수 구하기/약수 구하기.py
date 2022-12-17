n,k=map(int,input().split())
order=0
for i in range(1,n+1):
    if n%i==0:
        order+=1
        if order==k:
            print(i)
            exit()
print(0)