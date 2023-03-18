import sys
sys.setrecursionlimit(10**6)
nums=[]
def postorder(left,right):
    if left>right:
        return
    mid=right+1
    for i in range(left+1,right+1):
        if nums[left]<nums[i]:
            mid=i
            break
    postorder(left+1,mid-1)
    postorder(mid,right)
    print(nums[left])

while True:
    try:
        num=int(input())
        nums.append(num)
    except:
        break

postorder(0,len(nums)-1)