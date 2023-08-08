n=int(input())
a=list(map(int,input().split()))
arr=[a[0]]
for i in range(1,len(a)):
    if a[i]>arr[-1]:
        arr.append(a[i])
    else:
        left=0
        right=len(arr)
        while left<right:
            mid=(left+right)//2
            if a[i]<=arr[mid]:
                right=mid
            else:
                left=mid+1
        arr[right]=a[i]

print(len(arr))

