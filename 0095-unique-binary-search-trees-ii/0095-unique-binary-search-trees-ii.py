# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self,nums:List):
        if not nums:
            return [None]
        result=[]
        for i in range(len(nums)):
            left=self.buildTree(nums[:i])
            right=self.buildTree(nums[i+1:])
            for l in left:
                for r in right:
                    root=TreeNode(nums[i])
                    root.left=l
                    root.right=r
                    result.append(root)
        return result
        
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums=[num for num in range(1,n+1)]
        return self.buildTree(nums)
        