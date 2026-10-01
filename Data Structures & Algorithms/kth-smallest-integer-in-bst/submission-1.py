# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root, array):
        if not root:
            return
        array.append(root.val)
        self.traversal(root.left,array)
        self.traversal(root.right,array)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        self.traversal(root,array)

        return sorted(array)[k-1]
