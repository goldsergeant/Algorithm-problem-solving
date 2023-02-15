import sys

n=int(input())
nums=list(map(int,sys.stdin.readline().split()))
nums.sort()
m=int(input())
nums2=list(map(int,sys.stdin.readline().split()))
for num in nums2:
    left=0
    right=len(nums)-1
    flag=0
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<num:
            left=mid+1
        elif nums[mid]>num:
            right=mid-1
        else:
            flag=1
            break
    print(1 if flag==1 else 0)
