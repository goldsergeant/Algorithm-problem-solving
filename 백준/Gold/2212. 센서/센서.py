import sys

N=int(input())
K=int(input())
arr=list(map(int,sys.stdin.readline().rstrip().split()))
if K>=N:
    print(0)
    exit()

diff=[]

arr.sort()
for i in range(N-1):
    diff.append(arr[i+1]-arr[i])

diff.sort(reverse=True)
print(sum(diff[K-1:]))