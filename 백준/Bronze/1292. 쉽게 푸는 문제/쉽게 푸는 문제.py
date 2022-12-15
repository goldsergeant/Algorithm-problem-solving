import collections

n,m=map(int,input().split())
arr=[]
arr.append(0)
i=1
while i<1000:
    for a in range(i):
        arr.append(i)
    i+=1
print(sum(arr[n:m+1]))