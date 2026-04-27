# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertNode(self,root):
        print(root)
        if root is None:
            return
        else:
            root.left,root.right=root.right,root.left
            self.invertNode(root.left)
            self.invertNode(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.invertNode(root)
        return root
        