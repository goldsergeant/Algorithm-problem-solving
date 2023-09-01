a,b=map(int,input().split())
prime_numbers=[]
is_prime=[True for _ in range(b+1)]
answer=0
for i in range(2,b+1):
    if is_prime[i]:
        prime_numbers.append(i)
        for j in range(2*i,b+1,i):
            is_prime[j]=False

for i in range(a,b+1):
    if not is_prime[i]:
        tmp=[]
        while i>1:
            for prime in prime_numbers:
                if i%prime==0:
                    i/=prime
                    tmp.append(prime)
                    break
        if is_prime[len(tmp)]:
            answer+=1

print(answer)
