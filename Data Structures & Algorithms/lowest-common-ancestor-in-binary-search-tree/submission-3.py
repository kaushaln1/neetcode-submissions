# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, p, q, lca):
        if root:
            if p.val <= root.val <=q.val:
                # p 1 q =2 root 2 
                print("found" ,root.val)
                return root
            if root.val< p.val and root.val < q.val:
                print("right",root.val)
                return self.dfs(root.right, p, q, lca)  
            if root.val> p.val and root.val > q.val:
                print("left", root.val)
                return self.dfs(root.left, p,q, lca)
        else:
            print("Error")  

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p 
            p = q 
            q = temp
        return self.dfs(root, p ,q ,0)

        