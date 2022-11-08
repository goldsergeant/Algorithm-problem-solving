# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=collections.deque()
        queue.append(root)
        depth=0
        while queue:
            depth+=1
            for _ in range(len(queue)):
                root=queue.popleft()
                if not root.left and not root.right:
                    return depth
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)