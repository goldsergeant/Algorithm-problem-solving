import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
sum_arr=[arr[0]]
for i in range(1,len(arr)):
    sum_arr.append(sum_arr[i-1]+arr[i])

for _ in range(m):
    l,r=map(int,sys.stdin.readline().split())
    if l>1:
        print(sum_arr[r-1]-sum_arr[l-2])
    else:
        print(sum_arr[r-1])