# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maximum=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.maximum
    
    def height(self,root):
        if root is None:
            return 0
        else:
            length_right=self.height(root.right)
            length_left=self.height(root.left)
            length=max(length_right,length_left)
            self.maximum=max(self.maximum,length_left+length_right)
            return length+1