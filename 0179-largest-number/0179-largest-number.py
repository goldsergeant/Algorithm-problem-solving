class Solution:
    @staticmethod
    def swapable(n1:int,n2:int)->bool:
        return str(n1)+str(n2)>str(n2)+str(n1)
    def largestNumber(self, nums: List[int]) -> str:
        i=1
        while i<len(nums):
            j=i
            while j>0 and self.swapable(nums[j],nums[j-1]):
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1
            i+=1
        return str(int(''.join(map(str,nums))))
            
            
            