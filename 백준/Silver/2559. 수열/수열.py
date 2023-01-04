import sys

n,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
left,right=0,1
s=sum(arr[:k])
answer=[s]
for i in range(1,len(arr)-k+1):
    s=s-arr[i-1]+arr[i+k-1]
    answer.append(s)
print(max(answer))