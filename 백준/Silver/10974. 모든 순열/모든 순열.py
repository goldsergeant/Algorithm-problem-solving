import itertools

n=int(input())
arr=list(itertools.permutations([i for i in range(1,n+1)],n))

for i in arr:
    print(*i)
