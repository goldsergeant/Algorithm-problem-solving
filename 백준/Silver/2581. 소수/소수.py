prime_numbers=[]
m=int(input())
n=int(input())
check=[True for i in range(n+1)]
for i in range(2,n+1):
    if check[i]:
        if i>=m and i<=n:
            prime_numbers.append(i)
        for j in range(2*i,n+1,i):
            check[j]=False

if len(prime_numbers)>0:
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    print(-1)