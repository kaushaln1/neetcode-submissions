# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traversal(self, root1, root2):
        print( root1 , root2 )
        if (not root1) and (not root2):
            return True
        if not (root1 and root2) :
            return False

        if root1.val !=root2.val:
            return False
        
        l= self.traversal(root1.left, root2.left)
        r= self.traversal(root1.right, root2.right)
        if l and r :
            return True
        else:
            return False
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return self.traversal(p,q)
        