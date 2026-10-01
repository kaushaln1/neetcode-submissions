# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def bfs (self,node):
        if not node:
            return []
        resultarray=[]

        q = deque([node])

        while q:
            no_of_nodes = len(q)

            current_nodes = []
            for _ in range(no_of_nodes):
                current_node = q.popleft()
                current_nodes.append(current_node.val)
                if current_node.left :
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            
            resultarray.append(current_nodes)
        return resultarray

         
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        final = self.bfs(root)
        print (final)
        return final