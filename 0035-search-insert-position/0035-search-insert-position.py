class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if max(nums)<target:
                return len(nums)
            elif min(nums)>target:
                return 0
            else:
                for i in range(len(nums)):
                    if nums[i]<target<nums[i+1]:
                        return i+1