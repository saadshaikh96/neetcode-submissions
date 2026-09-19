# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced, maxHeight = self.dfs(root)
        return isBalanced

    def dfs(self, node):
        if not node:
            return [True, 0]
        leftBalanced, leftHeight = self.dfs(node.left)
        rightBalanced, rightHeight = self.dfs(node.right)

        isBalanced = leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1
        maxSubTreeHeight = 1 + max(leftHeight, rightHeight)

        return [isBalanced, maxSubTreeHeight]




        