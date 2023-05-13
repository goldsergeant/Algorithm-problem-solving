import sys

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))

if arr==sorted(arr):
    print(-1)
    exit()

for i in range(N-1,0,-1):
    if arr[i-1]>arr[i]:
        target=i-1
        for j in range(N-1,0,-1):
            if arr[target]>arr[j]:
                arr[target],arr[j]=arr[j],arr[target]
                print(*(arr[:target+1]+sorted(arr[target+1:],reverse=True)))
                exit()