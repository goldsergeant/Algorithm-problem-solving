import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
last_idx=0
answer=0
tmp=[0]*(N+1)

if A==B:
    print(1)
    exit()

def merge_sort(p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(p,q)
        merge_sort(q+1,r)
        merge(p,q,r)

def merge(p,q,r):
    global last_idx
    i,j,t=p,q+1,0
    while i<=q and j<=r:
        if A[i]<=A[j]:
            tmp[t]=A[i]
            i+=1
        else:
            tmp[t]=A[j]
            j+=1
        t+=1

    while i<=q:
        tmp[t]=A[i]
        t+=1
        i+=1
    while j<=r:
        tmp[t]=A[j]
        t+=1
        j+=1

    i,t=p,0
    while i<=r:
        flag=True
        if A[i]!=tmp[t] and i<last_idx:
            print(0)
            exit()
        A[i]=tmp[t]
        for idx in range(last_idx,N):
            if A[idx]!=B[idx]:
                flag=False
                last_idx=idx
                break
        if flag:
            print(1)
            exit()
        i+=1
        t+=1



merge_sort(0,N-1)
print(0)
