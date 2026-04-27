# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None :
            return True 
        if subRoot.val==root.val and self.Subtree(root,subRoot) :
                return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)


    def Subtree(self,root,subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        if root.val != subroot.val:
            return False
        return self.Subtree(root.left,subroot.left) and self.Subtree(root.right,subroot.right)


        