# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam=0
        queue=deque([root])
        while queue:
            cur=queue.pop()
            if cur is not None:
                queue.append(cur.right)
                queue.append(cur.left)   
                right=self.max_height(cur.right)
                left=self.max_height(cur.left)
                diam=max(diam,left+right)
        return diam

    def max_height(self,root):
        if root is None:
            return 0
        return(1+max(self.max_height(root.right),self.max_height(root.left)))
        