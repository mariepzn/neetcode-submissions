# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack=[(root,1)]
        max_depth=0
        while stack:
            pop,depth=stack.pop()
            max_depth=max(max_depth,depth)
            if pop.right:
                stack.append((pop.right,depth+1))
            if pop.left:                
                stack.append((pop.left,depth+1))
        return max_depth
            
        