# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    def traversal(self, root, lowerbound, upperbound):

        if not root:
            return True
        if  not lowerbound< root.val < upperbound:
            return False

        leftnode= self.traversal(root.left, lowerbound, root.val)
        rightnode = self.traversal(root.right, root.val, upperbound)

        return  leftnode & rightnode 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.traversal(root, float('-inf'), float('inf'))
