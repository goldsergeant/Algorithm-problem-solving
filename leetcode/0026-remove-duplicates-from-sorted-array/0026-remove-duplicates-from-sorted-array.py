class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=collections.Counter(nums)
        for i in counter:
            reps=counter[i]
            while reps>1:
                nums.remove(i)
                reps-=1
        return len(nums)