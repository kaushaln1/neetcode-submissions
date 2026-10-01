# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root,depth):
        if root:
            depth+=1
            l_dept= self.dfs(root.left,depth)
            r_dept =self.dfs(root.right,depth)
            depth = max(l_dept, r_dept)
        return depth
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        
        