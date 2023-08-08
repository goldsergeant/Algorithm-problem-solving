import bisect

n=int(input())
a=list(map(int,input().split()))
arr=[a[0]]
for i in range(1,len(a)):
    if a[i]>arr[-1]:
        arr.append(a[i])
    else:
        arr[bisect.bisect_left(arr,a[i])]=a[i]

print(len(arr))