class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
        def dfs(index,path):
            result.append(path)
            if len(nums)==index:
                return
            
            for i in range(index,len(nums)):
                dfs(i+1,path+[nums[i]])
                
        dfs(0,[])
        return result