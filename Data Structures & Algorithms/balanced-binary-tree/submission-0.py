# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True
        def dfs(root):
            nonlocal isBalance
            if not root:
                return 0
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
            if abs(rightDepth - leftDepth) > 1:
                isBalance = False    
            return max(rightDepth, leftDepth) + 1
        dfs(root)
        return isBalance