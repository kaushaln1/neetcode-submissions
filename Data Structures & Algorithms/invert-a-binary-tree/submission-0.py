# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_invert(self, root):
        if root:
            root.left , root.right = root.right, root.left
            self.dfs_invert(root.left)
            self.dfs_invert(root.right)
            return root

        return None
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs_invert(root)

        