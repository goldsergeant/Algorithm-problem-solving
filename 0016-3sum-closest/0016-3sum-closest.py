class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        currentClosest=sys.maxsize
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(currentClosest-target)>abs(total-target):
                    currentClosest=total
                if total>target:
                    right-=1
                elif total<target:
                    left+=1
                else:
                    return total
        return currentClosest