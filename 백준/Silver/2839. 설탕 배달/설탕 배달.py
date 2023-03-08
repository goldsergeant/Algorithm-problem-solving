import collections

n=int(input())

if n%5==0:
    print(n//5)
    exit()
else:
    count=0
    while n>0:
        n-=3
        count+=1
        if n%5==0:
            count+=n//5
            print(count)
            exit()
print(count if n==0 else -1)